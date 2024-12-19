import pyxel
import PyxelUniversalFont as puf
import json

dataFile = "savedata.json"

# jsonファイルからデータをロードする関数
def LoadData():
    try:
        # with 文を使うことにより，処理終了時にリソースの開放が自動で行われる．
        with open(dataFile, "r") as f:
            return json.load(f)
    # ファイルを開けなかった場合，タスク，得点無しと判定
    except FileNotFoundError:
        return None

# jsonファイルにデータを書き込む関数
def WriteData(data):
    with open(dataFile, "w") as f:
        json.dump(data, f)

class Character:
    def __init__(self, data):
        self.name = data["name"]
        self.maxHp = data["maxHp"]
        self.power = data["power"]
        self.guard = data["guard"]
        self.skills = data["skills"]
        self.exp = data["exp"]
        self.level = data["level"]
        self.positionX = 0
        self.positionY = 0

    def GetExp(self, exp):
        self.exp += exp
        if self.exp - 100 > 0:
            self.exp -= 100
            self.level += 1

    def Move(self, x, y):
        self.positionX += x
        self.positionY += y

class App():
    def __init__(self):
        pyxel.init(400, 300, title = "GridWalkAdventure")
        pyxel.mouse(True)
        self.writer = puf.Writer("IPA_PGothic.ttf")
        self.screen = "title"
        self.saveData = dataFile
        self.volume = 50
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.screen == "title":
            self.UpdateTitle()
        elif self.screen == "game":
            self.UpdateGame()
        elif self.screen == "option":
            self.UpdateOption()

    def draw(self):
        pyxel.cls(7)
        # 各モード画面の描画
        if self.screen == "title":
            self.DrawTitle()
        elif self.screen == "game":
            self.DrawGame()
        elif self.screen == "option":
            self.DrawOption()

    # タイトル画面の描画
    def DrawTitle(self):
        self.writer.draw(55, 80, "Grid Walk Adventure", 30, 2)
        pyxel.rect(120, 145, 150, 30, 11)
        self.writer.draw(130, 150, "ゲームスタート", 20, 2)
        pyxel.rect(120, 185, 150, 30, 11)
        self.writer.draw(150, 190, "オプション", 20, 2)
        pyxel.rect(120, 225, 150, 30, 11)
        self.writer.draw(145, 230, "ゲーム終了", 20, 2)

    def UpdateTitle(self):
        if pyxel.btnp(pyxel.KEY_1) or (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 120 < pyxel.mouse_x < 270 and 145 < pyxel.mouse_y < 175):
            self.screen = "game"
        elif pyxel.btnp(pyxel.KEY_2) or (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 120 < pyxel.mouse_x < 270 and 185 < pyxel.mouse_y < 215):
            self.screen = "option"
        elif pyxel.btnp(pyxel.KEY_Q) or (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 120 < pyxel.mouse_x < 270 and 225 < pyxel.mouse_y < 255):
            pyxel.quit()

    def UpdateOption(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.screen = "title"

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 210 < pyxel.mouse_x < 230 and 95 < pyxel.mouse_y <105:
            self.volume = max(0, self.volume - 1)
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 300 < pyxel.mouse_x < 320 and 95 < pyxel.mouse_y <105:
            self.volume = min(self.volume + 1, 100)

    def DrawOption(self):
        self.writer.draw(70, 90, "音量", 20, 2)
        pyxel.tri(210, 100, 230, 95, 230, 105, 2)
        self.writer.draw(250, 90, str(self.volume), 20, 2)
        pyxel.tri(320, 100, 300, 95, 300, 105, 2)

        self.writer.draw(130, 130, "Q : タイトルに戻る", 20, 2)

    def UpdateGame(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.screen = "title"

    def DrawGame(self):
        self.writer.draw(10, 10, "game", 20, 3)
        self.writer.draw(10, 130, "Q : タイトルに戻る", 20, 3)

App()