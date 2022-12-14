---
title: Crear rangos con nombre de ámbito de libro y hoja de trabajo
linktitle: Rango con nombre
type: docs
weight: 40
url: /es/net/create-workbook-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios definir rangos con nombre con dos ámbitos diferentes: libro de trabajo (también conocido como ámbito global) y hoja de trabajo.

- Se puede acceder a los rangos con nombre con un alcance de libro de trabajo desde cualquier hoja de trabajo dentro de ese libro simplemente usando su nombre.
- Se accede a los rangos con nombre en el ámbito de la hoja de trabajo con la referencia de la hoja de trabajo en particular en la que se creó.

Aspose.Cells proporciona la misma funcionalidad que Microsoft Excel para agregar rangos con nombre en el ámbito de libros y hojas de trabajo. Al crear un rango con nombre en el ámbito de la hoja de trabajo, la referencia de la hoja de trabajo debe usarse en el rango con nombre para especificarlo como un rango con nombre en el ámbito de la hoja de trabajo.

{{% /alert %}} 
## **Adición de un rango con nombre con el alcance del libro de trabajo**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Adición de un rango con nombre con ámbito de hoja de trabajo**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **Temas avanzados**
- [Crear acceso y copiar rangos con nombre](/cells/es/net/create-access-and-copy-named-ranges/)
- [Dar formato y modificar rangos con nombre](/cells/es/net/format-and-modify-named-ranges/)
- [Obtener rango con enlaces externos](/cells/es/net/get-range-with-external-links/)
- [Implementación de rangos no secuenciales](/cells/es/net/implementing-non-sequential-ranges/)
