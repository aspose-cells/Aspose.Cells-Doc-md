---
title: Proporcionar la ruta del archivo html de la hoja de cálculo exportada a través de la interfaz IFilePathProvider
type: docs
weight: 70
url: /es/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Escenarios de uso posibles**
Suponga que tiene un archivo de Excel con múltiples hojas y desea exportar cada hoja a un archivo HTML individual. Si alguna de sus hojas tiene enlaces a otras hojas, entonces esos enlaces estarán rotos en el HTML exportado. Para resolver este problema, Aspose.Cells proporciona la [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) interfaz que puede implementar para corregir los enlaces rotos.
## **Proporcione la ruta del archivo HTML de hoja de cálculo exportado a través de la interfaz IFilePathProvider**
Por favor, descargue el [archivo de Excel de muestra](5115213.zip) utilizado en el siguiente código y sus archivos HTML exportados. Todos estos archivos están dentro del directorio Temp. Debe extraerlos en la unidad C:. Luego se convertirá en el directorio C:\Temp. Luego abrirá el archivo Sheet1.html en el navegador y hacer clic en los dos enlaces que contiene. Estos enlaces se refieren a estas dos hojas de cálculo HTML exportadas que están dentro del directorio C:\Temp\OtherSheets.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

La siguiente captura de pantalla muestra cómo se ven los enlaces en C:\Temp\Sheet1.html y sus vínculos

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

La siguiente captura de pantalla muestra la fuente HTML. Como se puede ver, los enlaces ahora se refieren al directorio C:\Temp\OtherSheets. Esto se logró utilizando la interfaz [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Código de muestra**
Tenga en cuenta que el directorio C:\Temp es solo para fines ilustrativos. Puede usar cualquier directorio de su elección y colocar el [archivo de Excel de muestra](5115211.xlsx) dentro de él y ejecutar el código de ejemplo proporcionado. Luego creará el subdirectorio OtherSheets dentro de su directorio y exportará las hojas de cálculo HTML del segundo y tercer archivo dentro de él. Cambie la variable dirPath dentro del código proporcionado y refiérala al directorio de su elección antes de la ejecución.

{{% alert color="primary" %}} 

El código de ejemplo solo funcionará cuando se establezca la licencia de Aspose.Cells. Si intenta ejecutar el código sin establecer la licencia, entrará en un bucle infinito. Por lo tanto, hemos agregado una verificación para imprimir un mensaje y detener la ejecución cuando la licencia no está establecida. Puede adquirir una licencia o solicitar una licencia temporal de 30 días al equipo de Aspose.Purchase.

{{% /alert %}} 

Por favor note que comentar estas líneas dentro del código romperá los enlaces en Sheet1.html y Sheet2.html o Sheet3.html no se abrirán cuando se haga clic en sus enlaces dentro de Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Aquí está el código de ejemplo completo que se puede ejecutar con el [archivo de Excel de muestra](5115211.xlsx) proporcionado.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
