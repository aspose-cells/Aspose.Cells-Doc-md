---
title: Crear rangos con nombre a nivel de libro de trabajo y de hoja de cálculo
linktitle: Rango con nombre
type: docs
weight: 40
url: /es/net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios definir rangos con nombre con dos ámbitos diferentes: libro de trabajo (también conocido como ámbito global) y hoja de cálculo.

- Los rangos con nombre con ámbito de libro de trabajo se pueden acceder desde cualquier hoja de cálculo dentro de ese libro de trabajo simplemente utilizando su nombre.
- Los rangos con nombre de ámbito de hoja de cálculo se acceden con la referencia de la hoja de cálculo particular en la que se creó.

Aspose.Cells proporciona la misma funcionalidad que Microsoft Excel para agregar rangos con nombre a nivel de libro de trabajo y de hoja de cálculo. Al crear un rango con nombre de ámbito de hoja de cálculo, se debe utilizar la referencia de la hoja de cálculo en el rango con nombre para especificarlo como un rango con nombre de ámbito de hoja de cálculo.

{{% /alert %}} 
## **Agregar un Rango con Nombre de Alcance de Libro**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Agregar un Rango con Nombre de Alcance de Hoja de Cálculo**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **Temas avanzados**
- [Crear y Copiar Rangos con Nombre de Acceso](/cells/es/net/create-access-and-copy-named-ranges/)
- [Formato y Modificación de Rangos con Nombre](/cells/es/net/format-and-modify-named-ranges/)
- [Obtener Rango con Vínculos Externos](/cells/es/net/get-range-with-external-links/)
- [Implementación de Rangos No Secuenciales](/cells/es/net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="csharp" >}}
