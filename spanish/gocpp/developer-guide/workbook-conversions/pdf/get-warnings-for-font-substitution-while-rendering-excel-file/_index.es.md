---
title: Obtener advertencias de sustitución de fuente al renderizar archivo de Excel con Golang vía C++
linktitle: Obtener advertencias por sustitución de fuente
type: docs
weight: 230
url: /es/go-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Aprenda cómo obtener advertencias por sustitución de fuentes al renderizar archivos Excel a PDF usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

A veces, al renderizar un archivo Microsoft Excel a PDF, Aspose.Cells sustituye fuentes. Aspose.Cells proporciona una característica que permite a los desarrolladores saber qué fuente específica ha sido sustituida al activar una advertencia. Esta es una característica útil que puede ayudar a identificar por qué un PDF renderizado con Aspose.Cells se ve diferente al archivo original de Microsoft Excel, para que puedan tomar las acciones apropiadas. Por ejemplo, instalar las fuentes faltantes para que los resultados de renderizado se vean igual.

{{% /alert %}}

Para obtener advertencias por sustitución de fuentes al convertir archivos de Excel a PDF, implementa la interfaz `IWarningCallback` y establece la propiedad `PdfSaveOptions.WarningCallback` con la interfaz implementada.

La captura de pantalla a continuación muestra un archivo de Excel fuente que utilizaremos en el siguiente código. Tiene algo de texto en las celdas A6 y A7 en fuentes que no son renderizadas correctamente por Microsoft Excel.

|**No todas las fuentes se renderizan correctamente**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells sustituirá las fuentes en las celdas A6 y A7 con fuentes adecuadas como se muestra a continuación.

|**Fuentes Sustituidas**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Descargar Archivo Fuente y PDF de Salida**
Puedes descargar el archivo de Excel de origen y el PDF de salida desde los siguientes enlaces:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **Código**
El siguiente código implementa `IWarningCallback` y establece la propiedad `PdfSaveOptions.WarningCallback` con la interfaz implementada. Ahora, cada vez que alguna fuente sea sustituida en cualquier celda, Aspose.Cells generará una advertencia dentro del método `WarningCallback.Warning()`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWarningsForFontSubstitutionWhileRenderingExcelFile.go" >}}
## **Salida**
Después de convertir el archivo de Excel fuente a PDF, las advertencias se emiten en la consola de depuración de esta manera:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Si tu hoja de cálculo contiene fórmulas, es recomendable llamar al método `Workbook.CalculateFormula` justo antes de convertir la hoja a formato PDF. Hacer esto asegurará que los valores dependientes de fórmulas se recalcule y los valores correctos se muestren en el PDF.

{{% /alert %}}
