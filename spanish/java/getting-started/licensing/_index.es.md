---
title: Licencias
type: docs
weight: 50
url: /es/java/licensing/
description: Aspose.Cells for JAVA proporciona diferentes planes para compra u ofrece una Prueba Gratuita y una Licencia Temporal de 30 días para evaluación utilizando políticas de licenciamiento y suscripción en Java.
keywords: Aplicar licencia de Java desde disco o flujo. Establecer licencia de Java desde disco o flujo. Aplicar licencia en Aspose.Cells for Java.
---

## **Cómo Aplicar una Licencia en el Componente Aspose.Cells**

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, el número de desarrolladores con licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, por lo que no debe modificarlo; incluso la adición inadvertida de un salto de línea adicional en el archivo lo invalidará.

Debe configurar una licencia antes de utilizar Aspose.Cells si desea evitar sus limitaciones de evaluación. Solo es necesario configurar una licencia una vez por aplicación o proceso.

La licencia se puede cargar desde un flujo o archivo en las siguientes ubicaciones:

1. Ruta explícita.
1. La carpeta que contiene el Aspose.Cells.jar.

Usa el método [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense-java.io.InputStream-) para licenciar el componente. A menudo, la forma más sencilla de establecer una licencia es colocar el archivo de licencia en la misma carpeta que Aspose.Cells.jar y especificar solo el nombre del archivo sin la ruta, como se muestra en el siguiente ejemplo:

### **Cómo Aplicar una Licencia desde el Disco**

En este ejemplo, **Aspose.Cells** intentará encontrar el archivo de licencia en la carpeta que contiene los JAR de su aplicación.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Cómo Aplicar una Licencia desde un Flujo**

Inicializa una licencia desde un flujo.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Cómo Aplicar una Licencia en Aspose.Cells.GridWeb**

Se recomienda poner el código de licencia en un lugar de su aplicación web donde se procese primero.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Cómo aplicar una licencia medida**

Aspose.Cells permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de licencias. Este nuevo mecanismo de licencias se utilizará junto con el método de licenciamiento existente. Aquellos clientes que deseen ser facturados en función del uso de las funciones de la API pueden utilizar el licenciamiento medido. Para más detalles, consulte sección de [Preguntas frecuentes sobre Licenciamiento Medido](https://purchase.aspose.com/faqs/licensing/metered).

Se ha introducido una nueva clase [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) para aplicar una clave medida. A continuación se muestra un código de ejemplo que demuestra cómo configurar la clave pública y privada medida.

{{< highlight java >}}

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
{{< app/cells/assistant language="java" >}}
