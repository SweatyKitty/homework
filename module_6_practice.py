import arcade

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE='Pong Game'


class Ball(arcade.Sprite):
	def __init__(self):
		super().__init__('ball.png',0.05)
		self.change_x=3
		
	def update(self):#Список условий, чтобы мячик не вылетал за пределы окна
		self.center_x+=self.change_x
		self.center_y+=self.change_y
		if self.right>=SCREEN_WIDTH:
			self.change_x= -self.change_xq
		if self.left<=0:
			self.change_x=-self.change_x	
		if self.top>=SCREEN_HEIGHT:
			self.change_y=-self.change_y
		if self.bottom<=0:
			self.change_y=-self.change_y
			
class Bar(arcade.Sprite):#4На сайте arcade можно посмотреть аттрибуты для класса спрайт- нас интересуют filename и scale

	def __init__(self):
		super().__init__('bar.png',0.2)# 7 Ракетка вышла слишком большой, поэтому можно изменить параметр scale c 1.0 на 0.2
		#4Теперь чтобы эта ракуетка появилась в игре - нужно создать е] внутри класса game
	def update(self):
		self.center_x+=self.change_x
		if self.right>=SCREEN_WIDTH:
			self.right=SCREEN_WIDTH
		if self.left<=0:
			self.left=0
			

class Game(arcade.Window):#характеристики спрайт получает в ините, значит для его создания в game нужно и в game  переопределить init

	def __init__(self,width,height,title):
		super().__init__(width,height,title)
		self.bar=Bar()#Создание ракетки внутри класса game чтобы она появилась в игре
		self.setup()
		
	def setup(self):#6 создание метода, отвечающего за положение элементов в игре и размер
		self.bar.center_x=SCREEN_WIDTH/2
		self.bar.center_y=SCREEN_HEIGHT/5
		self.ball.center_x=SCREEN_WIDTH/2
		self.ball.center_y=SCREEN_HEIGHT/2
		
	def on_draw(self):    
		self.clear((255,255,255))#3 Переопределение метода on_draw c белым цветом фона окна
		self.bar.draw()#5 отрисовка ракетки в окне игры
		self.ball.draw()#8 отрисовка мяча в игре
	
	def update(self,delta):
		self.ball.update()
		self.bar.update()
		if arcade.check_for_collision(self.bar,self.ball):
			self.ball.change_y=-self.ball.change_y
		
	def on_key_press(self,key,modifiers):#метод позволяющий реагировать на мобытия зажатия кнопки, ниже для отжатия
		if key == arcade.key.RIGHT:
			self.bar.change_x=5
		if key == arcade.key.LEFT:
			self.bar.change_x=-5
	def on_key_release(self,key,modifiers):
		if key==arcade.key.RIGHT or key==arcade.key.LEFT:
			self.bar.change_x=0
			
	
	
if __name__=='__main__':
	window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)#1Создание экземпляра класса game31п4
#Окно из библиотеки pyglet принимает ряд параметров, нам интересны; ширина,высота и заголовок окна
	arcade.run()#2Запуск цикла обновлений "run" - В базе окно с черным фоном
	