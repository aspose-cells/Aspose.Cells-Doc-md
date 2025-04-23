---
title: Obtener Advertencias por Sustitución de Fuentes al Renderizar un Archivo de Excel
type: docs
weight: 120
url: /es/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

A veces, al renderizar archivos de Microsoft Excel a PDF, Aspose.Cells sustituye las fuentes. Aspose.Cells proporciona una función que permite a los desarrolladores saber que una fuente en particular ha sido sustituida mediante la emisión de una advertencia. Esta es una característica útil que puede ayudarte a identificar por qué el PDF renderizado por Aspose.Cells es diferente al archivo de Excel actual y luego puedes tomar acciones apropiadas. Por ejemplo, puedes instalar las fuentes faltantes para que los resultados del renderizado se vean iguales.

Si deseas obtener las advertencias por sustitución de fuentes al renderizar un archivo de Excel a PDF, implementa la interfaz IWarningCallback y establece el método setWarningCallback() de PdfSaveOptions con tu interfaz implementada.

{{% /alert %}}

La captura de pantalla a continuación muestra el archivo de Excel fuente utilizado en el siguiente código. Tiene algo de texto en las celdas A6 y A7 en fuentes que no son renderizadas correctamente por Microsoft Excel.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells sustituirá las fuentes en las celdas A6 y A7 con fuentes adecuadas como se muestra a continuación.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Descargar Archivo Fuente y PDF de Salida**

Puedes descargar el archivo de Excel fuente y el PDF de salida desde los siguientes enlaces

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

El siguiente código implementa el [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) y establece el método [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) con la interfaz implementada. Ahora, cada vez que se sustituya alguna fuente en cualquier celda, Aspose.Cells emitirá una advertencia dentro del método WarningCallback.warning().

{{< highlight java >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **Salida de Advertencias**

Después de convertir el archivo fuente, las siguientes advertencias se emiten en la consola de depuración:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

Si tu hoja de cálculo contiene fórmulas, es mejor llamar al método Workbook.calculateFormula justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, te asegurarás de que los valores dependientes de la fórmula se recalculen y los valores correctos se rendericen en el PDF. 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
