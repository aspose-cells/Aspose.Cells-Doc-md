---
title: Convalida l intero foglio di lavoro anziché solo le celle aggiornate
type: docs
weight: 80
url: /it/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **Possibili Scenari di Utilizzo**
Per impostazione predefinita, GridWeb convalida solo le celle aggiornate e non convalida l'intero foglio di lavoro. Tuttavia, se si desidera convalidare l'intero foglio di lavoro lato client prima che GridWeb invii la richiesta al server, è necessario impostare la variabile needValidateall all'interno di acwmain.js su true.
## **Convalida l'intero foglio di lavoro anziché solo le celle aggiornate**
La seguente schermata mostra la variabile needValidateall in acwmain.js. Si prega di impostarla su true e ora GridWeb convaliderà l'intero foglio di lavoro e non solo le celle aggiornate.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


