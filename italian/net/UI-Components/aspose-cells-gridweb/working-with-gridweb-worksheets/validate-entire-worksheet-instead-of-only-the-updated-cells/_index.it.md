---
title: Convalida l'intero foglio di lavoro anziché solo le celle aggiornate
type: docs
weight: 140
url: /it/net/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
## **Possibili scenari di utilizzo**
Per impostazione predefinita, GridWeb convalida solo le celle aggiornate e non convalida l'intero foglio di lavoro. Tuttavia, se si desidera convalidare l'intero foglio di lavoro sul lato client prima che GridWeb invii la richiesta al server, è necessario impostare la variabile needValidateall all'interno di acwmain.js su true.
## **Convalida l'intero foglio di lavoro anziché solo le celle aggiornate**
Lo screenshot seguente mostra la variabile needValidateall in acwmain.js. Impostalo su true e ora GridWeb convaliderà l'intero foglio di lavoro non solo le celle aggiornate.

![cose da fare:immagine_alt_testo](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)
