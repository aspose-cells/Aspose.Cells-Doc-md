---
title: Proporcione la ruta del archivo html de la hoja de trabajo exportada a través de la interfaz IFilePathProvider
type: docs
weight: 70
url: /es/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Posibles escenarios de uso**
 Supongamos que tiene un archivo de Excel con varias hojas y desea exportar cada hoja a un archivo HTML individual. Si alguna de sus hojas tiene enlaces a otras hojas, esos enlaces se romperán en el HTML exportado. Para solucionar este problema, Aspose.Cells proporciona[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)interfaz que puede implementar para reparar los enlaces rotos.
## **Proporcione la hoja de trabajo exportada HTML ruta del archivo a través de la interfaz IFilePathProvider**
 Por favor descarga el[ejemplo de archivo de Excel](5115213.zip)utilizado en el código siguiente y sus archivos HTML exportados. Todos estos archivos están dentro del directorio Temp. Debes extraerlo en la unidad C:. Entonces se convertirá en el directorio C:\Temp. Luego, abrirá el archivo Sheet1.html en el navegador y hará clic en los dos enlaces que contiene. Estos enlaces hacen referencia a estas dos hojas de trabajo HTML exportadas que se encuentran dentro del directorio C:\Temp\OtherSheets.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

La siguiente captura de pantalla muestra cómo se ven C:\Temp\Sheet1.html y sus enlaces

![todo:imagen_alternativa_texto](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 La siguiente captura de pantalla muestra la fuente HTML. Como puede ver, los enlaces ahora se refieren al directorio C:\Temp\OtherSheets. Esto se logró utilizando el[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)interfaz.

![todo:imagen_alternativa_texto](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Código de muestra**
 Tenga en cuenta que el directorio C:\Temp es solo para fines ilustrativos. Puede utilizar cualquier directorio de su elección y lugar[ejemplo de archivo de Excel](5115211.xlsx)dentro de allí y ejecute el código de muestra provisto. Luego creará el subdirectorio OtherSheets dentro de su directorio y exportará la segunda y tercera hoja de trabajo HTML dentro de él. Cambie la variable dirPath dentro del código provisto y consúltelo con el directorio de su elección antes de la ejecución.

{{% alert color="primary" %}} 

El código de muestra solo funcionará cuando configure la licencia Aspose.Cells. Si intenta ejecutar el código sin configurar la licencia, entrará en un bucle infinito. Por lo tanto, hemos agregado una verificación para imprimir un mensaje y detener la ejecución cuando la licencia no está configurada. Puede comprar una licencia o solicitar una licencia temporal de 30 días al equipo Aspose.Purchase.

{{% /alert %}} 

Consulte si comenta estas líneas dentro del código, se romperán los enlaces en Sheet1.html y Sheet2.html o Sheet3.html no se abrirán cuando se haga clic en sus enlaces dentro de Sheet1.html.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 Aquí está el código de muestra completo que se puede ejecutar con el proporcionado[ejemplo de archivo de Excel](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
