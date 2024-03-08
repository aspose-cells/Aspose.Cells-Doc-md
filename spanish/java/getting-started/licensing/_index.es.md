---
title: Licensing
type: docs
weight: 50
url: /es/java/licensing/
description: Aspose.Cells para JAVA proporciona diferentes planes de compra u ofrece una Prueba Gratuita y una Licencia Temporal de 30 días para evaluación utilizando Licensing y políticas de Suscripción en Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **Cómo aplicar una licencia en el componente Aspose.Cells**

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, la cantidad de desarrolladores para los que tiene licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifique; incluso la adición inadvertida de un salto de línea adicional al archivo lo invalidará.

Debe configurar una licencia antes de utilizar Aspose.Cells si desea evitar sus limitaciones de evaluación. Solo es necesario configurar una licencia una vez por solicitud o proceso.

La licencia se puede cargar desde una secuencia o archivo en las siguientes ubicaciones:

1. Camino explícito.
1. La carpeta que contiene Aspose.Cells.jar.

 Utilizar el[Licencia.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)método para licenciar el componente. A menudo, la forma más sencilla de configurar una licencia es colocar el archivo de licencia en la misma carpeta que Aspose.Cells.jar y especificar solo el nombre del archivo sin la ruta, como se muestra en el siguiente ejemplo:

###  **Cómo aplicar una licencia desde el disco**

 En este ejemplo**Aspose.Cells** Intentará encontrar el archivo de licencia en la carpeta que contiene los archivos JAR de su aplicación.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **Cómo solicitar una licencia de Stream**

Inicializa una licencia de una secuencia.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **Cómo solicitar una licencia en Aspose.Cells.GridWeb**

Se recomienda colocar el código de licencia en un lugar de su aplicación web donde deba procesarse primero.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Cómo solicitar una licencia medida**

Aspose.Cells permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de concesión de licencias. El nuevo mecanismo de concesión de licencias se utilizará junto con el método de concesión de licencias existente. Aquellos clientes que quieran que se les facture según el uso de las funciones API pueden utilizar la licencia medida. Para obtener más detalles, consulte[Preguntas frecuentes sobre el medidor Licensing](https://purchase.aspose.com/faqs/licensing/metered)sección.

una nueva clase[medido](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)Se ha introducido para aplicar la clave medida. A continuación se muestra el código de muestra que demuestra cómo configurar la clave pública y privada medida.

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
