from fractions import Fraction
import fractions
import matplotlib.pyplot as plt
import numpy
from decimal import Decimal

#全角とか整数値の時エラー吐くやつ書いてないけど半角小数で書いてくれさえすれば動くのでそこはどうにかしてほしい
print('xの値を半角かつ小数値で入力(例：3=3.0)\nデータとデータの間は半角スペースで')
x_li = list(map(Fraction,map(Decimal,input().split())))
print('yの値を半角かつ小数で入力(例：3=3.0)\nｘで入力したデータと同じ順番で\nデータとデータの間は半角スペースで')
y_li = list(map(Fraction,map(Decimal,input().split())))

print('x=' , x_li , 'y=' , y_li)

#2乗の関数
def double(n):
    return n**2

#Aを求める(どうせいらんけどのちのち使うかもしれんので)
A = list(map(double , y_li))
A = sum(A)

#Bを求める
B = list(map(double , x_li))
B = sum(B)

#Cを求める
C = sum(y_li)

#Dを求める
D = [x_li*y_li for(x_li , y_li) in zip(x_li , y_li)]
D = sum(D)

#Eを求める
E = sum(x_li)

E_2 = double(E)

#αを求める
a_bunbo = (4*B - E_2)
a_bunsi = (4*D - C*E)
a = Fraction(a_bunsi , a_bunbo)

#βを求める
b_bunbo = (4*B - E_2)
b_bunsi = (B*C - D*E)
b = Fraction(b_bunsi , b_bunbo)

#グラフタイトルに使うためにstr化
a_str = str(Fraction(a))
b_str = str(Fraction(b))

print('α=' , a , 'β=' , b)

#グラフ作成
x = numpy.linspace(0 , 10 , 10) #ここと一個下は適宜変えてくれ
plt.figure(0)
plt.grid(True)
plt.title('[y=αX+β]' + '(α=' + a_str + ' β=' + b_str + ') ' + 'y=(' + a_str + ')' + 'x+(' + b_str + ')')
plt.scatter(x_li , y_li , 5) #点をグラフ上に描画
plt.plot(x , (4*D - C*E) / (4*B - E_2) * x + (B*C - D*E) / (4*B - E_2) , C='orange') #回帰直線を描画、ここで計算しています
plt.show()

exit()