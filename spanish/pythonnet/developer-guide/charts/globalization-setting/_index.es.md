---
title: Convertir gráfico a imagen localizada con Python via .NET
linktitle: Establecer Región Localizada
type: docs
weight: 50
url: /es/python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: Aprende cómo configurar las configuraciones de globalización para los gráficos usando Aspose.Cells para Python via .NET. Configura los gráficos para soportar múltiples idiomas y formatos regionales para una correcta visualización del texto, fechas y números.
keywords: Aspose.Cells para Python via .NET, gráficos, configuraciones de globalización, múltiples idiomas, formatos regionales, visualización, texto, fechas, números.
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo convertir un gráfico en una imagen localizada y cómo establecer la región localizada para un gráfico.

{{% /alert %}}

## **Escenario**

¿Cuándo podrías necesitar establecer la región localizada para un gráfico?

Si abres un archivo XLSX con un gráfico en Excel con configuraciones regionales en español, elementos como el título y la leyenda del gráfico aparecerán en español. Sin embargo, guardar este gráfico como imagen usando Aspose.Cells podría hacer que estos elementos permanezcan en inglés por defecto:

**![Problema Global](GlobalIssue.png)**

Esto ocurre porque la leyenda del gráfico en la imagen de salida no coincide con la localización de Excel. Puedes resolverlo configurando las configuraciones de región localizada del gráfico.

## **Elementos compatibles**

Los siguientes elementos del gráfico se renderizarán de acuerdo con tus configuraciones de localización:

| **Elementos Compatibles**      | **Valor Predeterminado (Inglés)**       |
|-----------------------------|-----------------------------------|
| Nombre del Título del Eje             | Título del eje                        |
| Nombre de la Unidad del Eje              | Cientos, Miles...           |
| Nombre del Título del Gráfico            | Título del gráfico                       |
| Nombre del Aumento de la Leyenda        | Aumento                          |
| Nombre de la Disminución de la Leyenda        | Disminución                          |
| Nombre del Total de la Leyenda           | Total                             |
| Otro Nombre                  | Otro                             |
| Nombre de la Serie                 | Serie                            |

