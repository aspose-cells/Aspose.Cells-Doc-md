---
title: Marcadores Inteligentes en Encabezados y Pies de página | Aspose.Cells for Java
description: Coloque marcadores inteligentes en los encabezados y pies de página con la sintaxis de doble corchete angular y el interruptor WorkbookDesigner.setEnableHeaderFooterMarkers usando listas getter-bean o fuentes de datos JSON, y vincule imágenes mediante URIs de datos, en Aspose.Cells for Java.
linktitle: Marcadores Inteligentes en Encabezados y Pies de página | Aspose.Cells
keywords: Aspose.Cells for Java, Smart Markers, encabezados, pies de página, marcadores de encabezado y pie de página, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, getter bean, JSON data source, vinculación de datos, imagen, data URI, Java
type: docs
weight: 196
url: /es/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles Escenarios de Uso**
Los encabezados y pies de página suelen contener metadatos del informe, como el título del informe, el período de reporte, el autor y el departamento. Cuando esta información ya existe en la fuente de datos utilizada para rellenar el libro de trabajo, repetirla manualmente genera duplicación innecesaria.  
La sintaxis clásica de Marcador Inteligente, `&=Source.Field`, se procesa en las celdas del cuerpo de la hoja de cálculo. Si coloca un marcador clásico en un encabezado o pie de página mediante `PageSetup.setHeader` o `PageSetup.setFooter`, permanece como texto literal porque las cadenas de encabezado y pie de página no forman parte de la cuadrícula de celdas escaneada por `WorkbookDesigner.process()`.  
A partir de **Aspose.Cells for Java 26.11**, la opción de marcador de encabezado/pie de página de `WorkbookDesigner` es `false` de forma predeterminada. Llame a `designer.setEnableHeaderFooterMarkers(true)` antes de llamar a `designer.process()` para resolver marcadores escritos como `<<Source.Field>>` en las cadenas de sección de encabezado y pie de página. Los marcadores de encabezado y pie de página utilizan la misma fuente de datos que los marcadores del cuerpo.  
Cada encabezado y pie de página contiene tres secciones direccionables:
- La sección `0` es la sección izquierda.
- La sección `1` es la sección central.
- La sección `2` es la sección derecha.  
Utilice `PageSetup.setHeader(int section, String value)` y `PageSetup.setFooter(int section, String value)` para escribir estas secciones. Después del procesamiento, use `PageSetup.getHeader(int section)` y `PageSetup.getFooter(int section)` para obtener el texto completado.

{{% alert color="primary" %}}
Un marcador como `<<Source.Field>>` inserta el valor del campo como texto en la cadena de la sección. Las imágenes se vinculan con el sufijo `(picture)` y un valor de URI de datos.  
{{% /alert %}}

## **Habilitar Marcadores de Encabezado/Pie de Página con una Lista Getter-Bean**
Utilice la siguiente secuencia para resolver marcadores en encabezados y pies de página con una lista getter-bean en **Aspose.Cells for Java 26.11**:
1. Cree un `Workbook` y obtenga su primera `Worksheet` en el índice `0`, por ejemplo, con `workbook.getWorksheets().get(0)`.  
2. Escriba marcadores `<<Source.Field>>` en las secciones deseadas del encabezado y pie de página mediante `PageSetup.setHeader` y `PageSetup.setFooter`.  
3. Defina una pequeña clase **PUBLIC** bean con un getter (por ejemplo, `getName()`) para cada campo de marcador, y elija un nombre de fuente que coincida con el prefijo de fuente usado por los marcadores. Por ejemplo, una fuente llamada `node` respalda marcadores como `<<node.Name>>`. En esta plataforma se verifican dos reglas de enlace: un bean con CAMPOS públicos no enlaza nada (el motor lee getters, no campos), y una clase **PACKAGE-PRIVATE** tampoco enlaza nada — la introspección solo ve clases públicas, y un bean no público provoca que `process()` falle con una `NullPointerException`.  
4. Cree un `WorkbookDesigner` para el libro de trabajo.  
5. Llame a `designer.setEnableHeaderFooterMarkers(true)` antes del procesamiento.  
6. Adjunte la lista y su nombre de fuente con `designer.setDataSource("node", table)`.  
7. Llame a `designer.process()`.  
8. Después del procesamiento, los marcadores ya no aparecen en el texto del encabezado o pie de página. Utilice `PageSetup.getHeader` y `PageSetup.getFooter` para obtener las cadenas de sección completadas.  

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        private final String author;
        public Node(String name, String author) {
            this.name = name;
            this.author = author;
        }
        public String getName() {
            return name;
        }
        public String getAuthor() {
            return author;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Center header and center footer carry <<Source.Field>> placeholders
        worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
        worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
        List<Node> table = Arrays.asList(new Node("Q4 2026", "Aspose.Cells"));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", table);
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        System.out.println("Footer: " + worksheet.getPageSetup().getFooter(1));
        // This prints:
        // Header: Quarterly Report - Q4 2026
        // Footer: Prepared by Aspose.Cells
        workbook.save("HeaderFooterSmartMarkers.xlsx");
    }
}
```

## **Utilizar una Fuente de Datos JSON**
Puede usar JSON en lugar de una lista getter-bean cuando los datos del informe ya están disponibles en formato JSON. Llame a `WorkbookDesigner.setJsonDataSource(String name, String json)` para adjuntar la fuente.  
El argumento `name` es el nombre de fuente usado por los marcadores. Por ejemplo, el nombre `node` respalda marcadores como `<<node.Company>>` y `<<node.Title>>`.  
Passe los datos de fila directamente a `setJsonDataSource`:
- Se admite una matriz de filas, como una matriz JSON que contiene uno o más objetos de fila.  
- También puede pasarse directamente un único objeto de fila.  
- No envuelva las filas bajo una clave superior con nombre, como `{"rows":[...]}`. Este contenedor no es la forma esperada de entrada orientada a filas para este flujo de trabajo.  
Una fuente JSON puede poblar ambos estilos de marcadores durante la misma llamada a `designer.process()`. Puede resolver un marcador clásico `&=` en una celda del cuerpo y marcadores de doble corchete `<<>>` en secciones de encabezado y pie de página. Aún debe habilitar `EnableHeaderFooterMarkers` para que los marcadores de encabezado y pie de página se resuelvan.  

```java
import com.aspose.cells.*;
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Left header, right header, and a classic body marker — one JSON source feeds all three
        worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
        worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
        worksheet.getCells().get("A1").putValue("&=node.Company");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
        designer.process();
        System.out.println("Left: " + worksheet.getPageSetup().getHeader(0));
        System.out.println("Right: " + worksheet.getPageSetup().getHeader(2));
        System.out.println("Body: " + worksheet.getCells().get("A1").getStringValue());
        // This prints:
        // Left: Aspose Pty Ltd
        // Right: Page Half-Year Report
        // Body: Aspose Pty Ltd
        workbook.save("HeaderFooterJsonMarkers.xlsx");
    }
}
```

## **Semántica del Interruptor y Fuente Multi-Fila**
El ajuste `EnableHeaderFooterMarkers` es `false` de forma predeterminada, y el interruptor controla solo los marcadores de encabezado y pie de página `<<Source.Field>>`. Cuando el interruptor está desactivado, `designer.process()` sigue resolviendo los marcadores clásicos `&=` del cuerpo, pero un marcador `<<Source.Field>>` en un encabezado o pie de página permanece como texto literal.  
Una sección de encabezado o pie de página es una sola cadena, no una banda repetitiva. Si la fuente de datos contiene varias filas, la primera fila suministra los valores de encabezado y pie de página. Una vez resueltos, los valores se convierten en texto ordinario de encabezado o pie de página. Permanecen en el libro de trabajo después de llamar a `workbook.save(...)` y están presentes cuando se vuelve a cargar el libro guardado.  
El siguiente ejemplo crea dos libros de trabajo sobre la misma lista de beans multi-fila para contrastar el comportamiento deshabilitado y habilitado. El `plainDesigner` deja el marcador sin cambios, mientras que el `enabledDesigner` lo resuelve usando la primera fila.  

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        public Node(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
    public static void main(String[] args) throws Exception {
        List<Node> table = Arrays.asList(
                new Node("First Row"),
                new Node("Second Row")
        );
        // Without the switch the placeholder stays literal text
        Workbook plainWorkbook = new Workbook();
        Worksheet plainSheet = plainWorkbook.getWorksheets().get(0);
        plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
        plainDesigner.setDataSource("node", table);
        plainDesigner.process();
        // With the switch on, the FIRST row of a multi-row source wins
        Workbook enabledWorkbook = new Workbook();
        Worksheet enabledSheet = enabledWorkbook.getWorksheets().get(0);
        enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
        enabledDesigner.setEnableHeaderFooterMarkers(true);
        enabledDesigner.setDataSource("node", table);
        enabledDesigner.process();
        System.out.println("Without switch: " + plainSheet.getPageSetup().getHeader(1));
        System.out.println("With switch: " + enabledSheet.getPageSetup().getHeader(1));
        // This prints:
        // Without switch: <<node.Name>>
        // With switch: First Row
        enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
    }
}
```

## **Vincular una Imagen en un Encabezado o Pie de Página**
El sufijo `(picture)` vincula una imagen a una sección de encabezado o pie de página. Escriba `<<node.logo(picture)>>` donde debe aparecer la imagen y proporcione el valor del campo como una URI de datos — el prefijo `data:image/png;base64,` seguido del texto Base64 de los bytes de la imagen. Una cadena Base64 sin el prefijo `data:` no incrusta una imagen.  
Después de `designer.process()`:
1. El marcador se reemplaza por `&G`, el código estándar de encabezado y pie de página para imágenes. Como el marcador se convierte en un código dentro de la cadena de la sección, puede coexistir con texto más largo, por ejemplo `Logo: <<node.logo(picture)>>`.  
2. Los bytes de la imagen se incrustan en el libro de trabajo como una parte multimedia adjunta a la capa de dibujo de encabezado/pie de página de esa hoja, de modo que la imagen se imprime junto con el encabezado o pie de página.  

```java
import com.aspose.cells.*;
import java.nio.file.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String logo;
        public Node(String logo) {
            this.logo = logo;
        }
        public String getLogo() {
            return logo;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // The (picture) suffix binds the image named by the data-URI field into the header
        worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
        String logoDataUri = "data:image/png;base64," + Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("logo.png")));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", Arrays.asList(new Node(logoDataUri)));
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        // This prints:
        // Header: Logo: &G
        workbook.save("HeaderFooterPicture.xlsx");
    }
}
```

El `&G` impreso es el código de imagen que Excel interpreta al renderizar el encabezado — los bytes de `logo.png` ahora residen dentro de `HeaderFooterPicture.xlsx`, y la imagen se imprime en lugar del código.  
Para usar marcadores inteligentes en encabezados y pies de página, escriba marcadores `<<Source.Field>>` en las secciones izquierda, central y derecha del encabezado o pie de página con `PageSetup.setHeader` y `PageSetup.setFooter`. Llame a `designer.setEnableHeaderFooterMarkers(true)` en el `WorkbookDesigner` antes de llamar a `designer.process()`, y proporcione valores mediante `designer.setDataSource(name, list)` con una lista getter-bean o `designer.setJsonDataSource(name, json)`. Lea las secciones completadas con `PageSetup.getHeader` y `PageSetup.getFooter`. La misma fuente de datos puede poblar marcadores del cuerpo y marcadores de encabezado o pie de página en una única pasada de procesamiento. Añada el sufijo `(picture)` con un valor de URI de datos para vincular una imagen a una sección.

## **Artículos Relacionados**
- [Renderizado de Matriz de Célula Única con SmartMarker](/cells/es/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}