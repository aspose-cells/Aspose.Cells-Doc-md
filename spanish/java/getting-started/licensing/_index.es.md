---
title: Licencia
type: docs
weight: 50
url: /es/java/licensing/
---
{{% alert color="primary" %}} 

 Puede descargar una versión de evaluación de**Aspose.Cells** for Java desde[su pagina de descarga](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. La versión de evaluación proporciona absolutamente las mismas capacidades que la versión con licencia del producto. Además, la versión de evaluación simplemente obtiene la licencia cuando compra una licencia y agrega un par de líneas de código para aplicar la licencia.

 Una vez que esté satisfecho con su evaluación de**Aspose.Cells** , puedes[comprar una licencia](https://purchase.aspose.com)en el sitio web Aspose. Familiarícese con los diferentes tipos de suscripción que se ofrecen. Si tiene alguna pregunta, no dude en ponerse en contacto con el equipo de ventas Aspose.

Cada licencia Aspose incluye una suscripción de un año para actualizaciones gratuitas a cualquier nueva versión o corrección que surja durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como a usuarios de evaluación.

{{% /alert %}} {{% alert color="primary" %}} 

 Si quieres probar**Aspose.Cells** sin limitaciones de versión de evaluación, solicite una licencia temporal de 30 días. Por favor refiérase a[¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license) para más información.

{{% /alert %}}

## **Limitaciones de la versión de evaluación**

 Versión de evaluación de**Aspose.Cells** El producto (sin una licencia especificada) proporciona la funcionalidad completa del producto, pero está limitado a abrir 100 archivos en un programa y una hoja de trabajo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

### **1ra Limitación: Número de Archivos Abiertos**

Al ejecutar su programa, solo puede abrir 100 archivos de Excel. Si su aplicación excede este número, se lanzará una excepción.

### **2da Limitación: Hoja de Trabajo con Marca de Agua de Evaluación**

![todo:imagen_alternativa_texto](licensing_1.png)

Esta hoja de trabajo siempre se mostrará como la hoja de trabajo activa. Solo en la versión con licencia, puede configurar la hoja de trabajo activa en otras hojas de trabajo.

## **Configuración de una licencia**

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, la cantidad de desarrolladores para los que tiene licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no modifique el archivo; incluso la adición inadvertida de un salto de línea adicional en el archivo lo invalidará.

Debe configurar una licencia antes de utilizar Aspose.Cells si desea evitar sus limitaciones de evaluación. Solo debe establecer una licencia una vez por aplicación o proceso.

La licencia se puede cargar desde un flujo o archivo en las siguientes ubicaciones:

1. Camino explícito.
1. La carpeta que contiene el Aspose.Cells.jar.

 Utilizar el[Licencia.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) para obtener la licencia del componente. A menudo, la forma más fácil de configurar una licencia es colocar el archivo de licencia en la misma carpeta que Aspose.Cells.jar y especificar solo el nombre del archivo sin la ruta, como se muestra en el siguiente ejemplo:

### **Ejemplo 1**

 En este ejemplo**Aspose.Cells** intentará encontrar el archivo de licencia en la carpeta que contiene los archivos JAR de su aplicación.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Ejemplo 2**

Inicializa una licencia de una secuencia.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Notas sobre la aplicación de una licencia en Aspose.Cells.GridWeb**

Se recomienda colocar el código de licencia en un lugar de su aplicación web donde deba procesarse primero.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Aplicación de licencia medida**

Aspose.Cells permite a los desarrolladores aplicar la clave medida. Es un nuevo mecanismo de licencia. El nuevo mecanismo de concesión de licencias se utilizará junto con el método de concesión de licencias existente. Aquellos clientes que deseen que se les facture en función del uso de las funciones API pueden utilizar la licencia medida. Para obtener más detalles, consulte[Preguntas frecuentes sobre licencias medidas](https://purchase.aspose.com/faqs/licensing/metered)sección.

una nueva clase[medido](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)se ha introducido para aplicar la clave medida. El siguiente es el código de muestra que demuestra cómo establecer una clave pública y privada medida.

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
