---
title: Valide toda la hoja de trabajo en lugar de solo las celdas actualizadas
type: docs
weight: 80
url: /es/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
## **Posibles escenarios de uso**
De forma predeterminada, GridWeb valida solo las celdas actualizadas y no valida toda la hoja de trabajo. Sin embargo, si desea validar toda la hoja de trabajo en el lado del cliente antes de que GridWeb publique la solicitud en el servidor, debe establecer la variable needValidateall dentro de acwmain.js en verdadero.
## **Valide toda la hoja de trabajo en lugar de solo las celdas actualizadas**
La siguiente captura de pantalla muestra la variable needValidateall en acwmain.js. Establézcalo en verdadero y ahora GridWeb validará toda su hoja de trabajo, no solo las celdas actualizadas.

![todo:imagen_alternativa_texto](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


