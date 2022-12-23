---
title: Obtenga advertencias para la sustitución de fuentes mientras procesa un archivo de Excel
type: docs
weight: 230
url: /es/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

veces, al representar un archivo de Excel Microsoft en PDF, Aspose.Cells sustituye las fuentes. Aspose.Cells proporciona una función que les permite a los desarrolladores saber qué fuente en particular se ha sustituido mediante la activación de una advertencia. Esta es una característica útil que puede ayudarlo a identificar por qué un Aspose.Cells renderizado PDF se ve diferente del archivo de Excel Microsoft original para que pueda tomar las medidas apropiadas. Por ejemplo, instalar las fuentes que faltan para que los resultados de renderizado se vean iguales.

{{% /alert %}} 

Para recibir advertencias sobre la sustitución de fuentes al representar archivos de Excel en PDF, implemente la interfaz IWarningCallback y configure la propiedad PdfSaveOptions.WarningCallback con su interfaz implementada.

La siguiente captura de pantalla muestra un archivo fuente de Excel que usaremos en el siguiente código. Tiene algo de texto en las celdas A6 y A7 en fuentes que Microsoft Excel no reproduce bien.

|**No todas las fuentes se representan correctamente**|
|:- |
|![todo:imagen_alternativa_texto](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells sustituirá las fuentes en las celdas A6 y A7 con fuentes adecuadas como se muestra a continuación.

|**Fuentes sustituidas**|
|:- |
|![todo:imagen_alternativa_texto](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Descargar archivo fuente y salida PDF**
Puede descargar el archivo fuente de Excel y la salida PDF desde los siguientes enlaces

- [fuente.xlsx](5112611.xlsx)
- [salida.pdf](5112616.pdf)
## **Código**
El siguiente código implementa IWarningCallback y establece la propiedad PdfSaveOptions.WarningCallback con la interfaz implementada. Ahora, cada vez que se sustituya cualquier fuente en cualquier celda, Aspose.Cells activará una advertencia dentro del método WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Producción**
Después de convertir el archivo de origen de Excel a PDF, las advertencias se envían a la consola de depuración de esta manera:

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar al método Workbook.CalculateFormula justo antes de convertir la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
