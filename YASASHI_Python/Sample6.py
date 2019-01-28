#class use
import myclass

pr = myclass.Customer("鈴木", 23, "aaa@bbb.cc.jp", "123-456-7890")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, "さんは", ag, "才です。")
print("アドレスは", ad, "電話番号は", tl, "です。")