---
title: Validera hela kalkylbladet istället för bara de uppdaterade cellerna
type: docs
weight: 140
url: /sv/net/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
## **Möjliga användningsscenarier**
Som standard validerar GridWeb endast de uppdaterade cellerna och validerar inte hela kalkylbladet. Men om du vill validera hela kalkylbladet på klientsidan innan GridWeb skickar en begäran till servern, bör du ställa in variabeln needValidateall inuti acwmain.js till true.
## **Validera hela kalkylbladet istället för bara de uppdaterade cellerna**
Följande skärmdump visar variabeln needValidateall i acwmain.js. Vänligen ställ in det på sant och nu kommer GridWeb att validera hela ditt kalkylblad, inte bara de uppdaterade cellerna.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)
