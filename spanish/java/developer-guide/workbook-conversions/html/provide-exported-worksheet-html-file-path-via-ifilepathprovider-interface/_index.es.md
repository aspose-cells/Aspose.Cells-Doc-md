---
title: Proporcionar la ruta del archivo HTML de la hoja de cálculo exportada a través de la interfaz IFilePathProvider
type: docs
weight: 870
url: /es/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Escenarios de uso posibles**
Supongamos que tiene un archivo de Excel con varias hojas y quiere exportar cada hoja a un archivo HTML individual. Si alguna de sus hojas contiene enlaces a otras hojas, entonces esos enlaces se romperán en el HTML exportado. Para solucionar este problema, Aspose.Cells proporciona la interfaz [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider) que puede implementar para reparar los enlaces rotos.
## **Proporcione la ruta del archivo HTML de hoja de cálculo exportado a través de la interfaz IFilePathProvider**
Por favor, descargue el [archivo de Excel de ejemplo](5473417.zip) utilizado en el siguiente código y sus archivos HTML exportados. Todos estos archivos están dentro del directorio *Temp*. Debería extraerlo en la unidad *C:*. Luego se convertirá en el directorio *C:\Temp*. Luego abrirá el archivo *Sheet1.html* en el navegador y hará clic en los dos enlaces dentro. Estos enlaces se refieren a las dos hojas de cálculo HTML exportadas que están dentro del directorio *C:\Temp\OtherSheets*.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

La siguiente captura de pantalla muestra cómo se ve el *C:\Temp\Sheet1.html* y sus enlaces

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

La siguiente captura de pantalla muestra la fuente HTML. Como se puede ver, los enlaces ahora hacen referencia al directorio *C:\Temp\OtherSheets*. Esto se logró utilizando la interfaz [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Código de muestra**
Por favor, ten en cuenta que el directorio *C:\Temp* es solo para fines ilustrativos. Puedes usar cualquier directorio de tu elección y colocar el [archivo de Excel de muestra](5473414.xlsx) dentro de él y ejecutar el código de ejemplo proporcionado. A continuación, se creará un subdirectorio *OtherSheets* dentro de tu directorio y se exportarán los segundos y terceros libros de trabajo en formato HTML dentro de él. Por favor, cambia la variable *dirPath* dentro del código proporcionado y refiérela al directorio de tu elección antes de la ejecución.

{{% alert color="primary" %}} 

El código de ejemplo solo funcionará cuando se establezca la licencia de Aspose.Cells. Si intenta ejecutar el código sin establecer la licencia, entrará en un bucle infinito. Por lo tanto, hemos agregado una verificación para imprimir un mensaje y detener la ejecución cuando la licencia no está establecida. Puede adquirir una licencia o solicitar una licencia temporal de 30 días al equipo de Aspose.Purchase.

{{% /alert %}} 

Por favor, ten en cuenta que comentar estas líneas dentro del código romperá los enlaces en *Sheet1.html* y *Sheet2.html* o *Sheet3.html* no se abrirán cuando se haga clic en sus enlaces dentro de *Sheet1.html*



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



Aquí tienes el código de ejemplo completo que puedes ejecutar con el [archivo de Excel de muestra](5473414.xlsx) proporcionado.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
{{< app/cells/assistant language="java" >}}
