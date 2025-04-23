---
title: Obtener Advertencias por Sustitución de Fuentes al Renderizar un Archivo de Excel
type: docs
weight: 230
url: /es/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

A veces, al renderizar un archivo Microsoft Excel a PDF, Aspose.Cells sustituye fuentes. Aspose.Cells proporciona una característica que permite a los desarrolladores saber qué fuente específica ha sido sustituida al activar una advertencia. Esta es una característica útil que puede ayudar a identificar por qué un PDF renderizado con Aspose.Cells se ve diferente al archivo original de Microsoft Excel, para que puedan tomar las acciones apropiadas. Por ejemplo, instalar las fuentes faltantes para que los resultados de renderizado se vean igual.

{{% /alert %}} 

Para obtener advertencias por sustitución de fuentes al renderizar archivos de Excel a PDF, implemente la interfaz IWarningCallback y establezca la propiedad PdfSaveOptions.WarningCallback con su interfaz implementada.

La captura de pantalla a continuación muestra un archivo de Excel fuente que utilizaremos en el siguiente código. Tiene algo de texto en las celdas A6 y A7 en fuentes que no son renderizadas correctamente por Microsoft Excel.

|**No todas las fuentes se renderizan correctamente**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells sustituirá las fuentes en las celdas A6 y A7 con fuentes adecuadas como se muestra a continuación.

|**Fuentes Sustituidas**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Descargar Archivo Fuente y PDF de Salida**
Puedes descargar el archivo de Excel fuente y el PDF de salida desde los siguientes enlaces

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **Código**
El siguiente código implementa la interfaz IWarningCallback y establece la propiedad PdfSaveOptions.WarningCallback con la interfaz implementada. Ahora, cada vez que se sustituya alguna fuente en alguna celda, Aspose.Cells generará una advertencia dentro del método WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Salida**
Después de convertir el archivo de Excel fuente a PDF, las advertencias se emiten en la consola de depuración de esta manera:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar al método Workbook.CalculateFormula justo antes de renderizar la hoja de cálculo al formato PDF. Haciendo esto, asegurará que los valores dependientes de las fórmulas se recalculen y se rendericen los valores correctos en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
