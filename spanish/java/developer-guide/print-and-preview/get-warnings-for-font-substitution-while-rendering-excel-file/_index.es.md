---
title: Obtenga advertencias para la sustitución de fuentes mientras procesa un archivo de Excel
type: docs
weight: 120
url: /es/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

A veces, al renderizar Microsoft archivos de Excel a PDF, Aspose.Cells sustituye las fuentes. Aspose.Cells proporciona una función que les permite a los desarrolladores saber que una fuente en particular ha sido sustituida al activar una advertencia. Esta es una característica útil que puede ayudarlo a identificar por qué Aspose.Cells representado PDF es diferente al archivo de Excel real y luego puede tomar las medidas apropiadas. Por ejemplo, puede instalar las fuentes que faltan para que los resultados de la representación tengan el mismo aspecto.

Si desea obtener las advertencias para la sustitución de fuentes mientras procesa un archivo de Excel en PDF, implemente la interfaz IWarningCallback y configure el método PdfSaveOptions.setWarningCallback() con su interfaz implementada.

{{% /alert %}}

La siguiente captura de pantalla muestra el archivo fuente de Excel utilizado en el siguiente código. Tiene algo de texto en las celdas A6 y A7 en fuentes que Microsoft Excel no representa bien.

![todo:imagen_alternativa_texto](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells sustituirá las fuentes en las celdas A6 y A7 con fuentes adecuadas como se muestra a continuación.

![todo:imagen_alternativa_texto](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Descargar archivo fuente y salida PDF**

Puede descargar el archivo fuente de Excel y la salida PDF desde los siguientes enlaces

- [fuente.xlsx](5472700.xlsx)
- [salida.pdf](5472699.pdf)

 El siguiente código implementa el[**IAdvertenciaDevolución de llamada**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) y establecer el[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) método con la interfaz implementada. Ahora, cada vez que se sustituya una fuente en cualquier celda, Aspose.Cells activará una advertencia dentro del método WarningCallback.warning().

{{< highlight "java" >}}

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

## **Salida de advertencias**

Después de convertir el archivo de origen, se envían las siguientes advertencias a la consola de depuración:

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar al método Workbook.calculateFormula justo antes de convertir la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
