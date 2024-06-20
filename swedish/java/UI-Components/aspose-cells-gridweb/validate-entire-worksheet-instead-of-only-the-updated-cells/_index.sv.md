---
title: Validera hela arbetsbladet istället för endast uppdaterade celler
type: docs
weight: 80
url: /sv/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **Möjliga användningsscenario**
Som standard validerar GridWeb endast de uppdaterade cellerna och validerar inte hela arbetsbladet. Om du vill validera hela arbetsbladet på klientsidan innan GridWeb begär att servern, bör du sätta needValidateAll-variabeln inuti acwmain.js till true.
## **Validera hela arbetsbladet istället för endast uppdaterade celler**
Följande skärmbild visar needValidateAll-variabeln i acwmain.js. Vänligen ställ in den till true och nu kommer GridWeb att validera hela arbetsbladet inte bara de uppdaterade cellerna.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


