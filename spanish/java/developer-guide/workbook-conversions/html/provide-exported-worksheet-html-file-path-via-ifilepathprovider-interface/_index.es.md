---
title: Proporcione la ruta del archivo HTML de la hoja de trabajo exportada a través de la interfaz IFilePathProvider
type: docs
weight: 870
url: /es/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Posibles escenarios de uso**
 Supongamos que tiene un archivo de Excel con varias hojas y desea exportar cada hoja a un archivo HTML individual. Si alguna de sus hojas tiene enlaces a otras hojas, esos enlaces se romperán en el HTML exportado. Para hacer frente a este problema, Aspose.Cells proporciona[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)interfaz que puede implementar para reparar los enlaces rotos.
## **Proporcione la ruta del archivo HTML de la hoja de trabajo exportada a través de la interfaz IFilePathProvider**
 Por favor descarga el[ejemplo de archivo de Excel](5473417.zip) utilizado en el siguiente código y sus archivos HTML exportados. Todos estos archivos están dentro del*Temperatura* directorio. Deberías extraerlo en*C:* conducir. Entonces se convertirá*C:\Temp*directorio. Luego abrirás el*Hoja1.html* archivo en el navegador y haga clic en los dos enlaces dentro de él. Estos enlaces se refieren a estas dos hojas de trabajo HTML exportadas que están dentro del*C:\Temp\Otras hojas*directorio.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

La siguiente captura de pantalla muestra cómo el*C:\Temp\Hoja1.html*y sus enlaces parecen

![todo:imagen_alternativa_texto](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 La siguiente captura de pantalla muestra la fuente HTML. Como puede ver, los enlaces ahora se refieren a*C:\Temp\Otras hojas* directorio. Esto se logró utilizando el[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)interfaz.

![todo:imagen_alternativa_texto](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Código de muestra**
 tenga en cuenta*C:\Temp* El directorio es solo para fines ilustrativos. Puede utilizar cualquier directorio de su elección y lugar[ejemplo de archivo de Excel](5473414.xlsx) dentro de allí y ejecute el código de muestra provisto. Entonces creará*Otras hojas* subdirectorio dentro de su directorio y exporte la segunda y tercera hojas de trabajo HTML dentro de él. Por favor cambie el*dirPath*variable dentro del código provisto y remítalo al directorio de su elección antes de la ejecución.

{{% alert color="primary" %}} 

El código de muestra solo funcionará cuando configure la licencia Aspose.Cells. Si intenta ejecutar el código sin configurar la licencia, entrará en un bucle infinito. Por lo tanto, hemos agregado una verificación para imprimir un mensaje y detener la ejecución cuando la licencia no está configurada. Puede comprar una licencia o solicitar una licencia temporal de 30 días al equipo Aspose.Purchase.

{{% /alert %}} 

 Por favor vea comentar estas líneas dentro del código romperá los enlaces en*Hoja1.html* y*Hoja2.html* o*Hoja3.html*no se abrirá cuando se haga clic en sus enlaces dentro del*Hoja1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



 Aquí está el código de muestra completo que puede ejecutar con el proporcionado[ejemplo de archivo de Excel](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
