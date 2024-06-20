---
title: Crear rangos con nombre a nivel de libro de trabajo y de hoja de cálculo
linktitle: Rango con nombre
type: docs
weight: 40
url: /es/python-net/create-workbook-and-worksheet-scoped-named-ranges/
description: Este artículo muestra cómo crear Rangos Nombrados con alcance de Libro y Hoja utilizando la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Crear Rangos Nombrados con alcance de Libro y Hoja en Python, Agregar un Rango Nombrado con alcance de Libro en Python, Agregar un Rango Nombrado con alcance de Hoja en Python.
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios definir rangos con nombre con dos ámbitos diferentes: libro de trabajo (también conocido como ámbito global) y hoja de cálculo.

- Los rangos con nombre con ámbito de libro de trabajo se pueden acceder desde cualquier hoja de cálculo dentro de ese libro de trabajo simplemente utilizando su nombre.
- Los rangos con nombre de ámbito de hoja de cálculo se acceden con la referencia de la hoja de cálculo particular en la que se creó.

Aspose.Cells for Python via .NET proporciona la misma funcionalidad que Microsoft Excel para añadir rangos nombrados con alcance de libro y hoja. Cuando se crea un rango nombrado con alcance de hoja, se debe usar la referencia a la hoja de cálculo en el rango nombrado para especificarlo como un rango nombrado con alcance de hoja.


{{% /alert %}} 
## **Cómo Agregar un Rango Nombrado con Alcance de Libro**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.py" >}}
## **Cómo Agregar un Rango Nombrado con Alcance de Hoja**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-WorksheetNamedRange-1.py" >}}

## **Temas avanzados**
- [Crear y Copiar Rangos con Nombre de Acceso](/cells/es/python-net/create-access-and-copy-named-ranges/)
- [Formato y Modificación de Rangos con Nombre](/cells/es/python-net/format-and-modify-named-ranges/)
- [Obtener Rango con Vínculos Externos](/cells/es/python-net/get-range-with-external-links/)
- [Implementación de Rangos No Secuenciales](/cells/es/python-net/implementing-non-sequential-ranges/)
