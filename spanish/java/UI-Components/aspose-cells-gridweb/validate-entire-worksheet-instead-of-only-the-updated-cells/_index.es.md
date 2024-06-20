---
title: Validar toda la hoja de cálculo en lugar de solo las celdas actualizadas
type: docs
weight: 80
url: /es/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **Escenarios de uso posibles**
Por defecto, GridWeb valida solo las celdas actualizadas y no valida toda la hoja de cálculo. Sin embargo, si desea validar toda la hoja de cálculo en el lado del cliente antes de que GridWeb envíe una solicitud al servidor, entonces debe establecer la variable needValidateAll dentro del acwmain.js como verdadera.
## **Validar toda la hoja de cálculo en lugar de solo las celdas actualizadas**
La siguiente captura de pantalla muestra la variable needValidateAll en acwmain.js. Establézcala como verdadera y ahora GridWeb validará toda su hoja de cálculo no solo las celdas actualizadas.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


