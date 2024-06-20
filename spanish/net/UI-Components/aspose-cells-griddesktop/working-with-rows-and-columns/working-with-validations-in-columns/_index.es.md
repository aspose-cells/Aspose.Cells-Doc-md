---
title: Trabajar con Validaciones en Columnas
type: docs
weight: 80
url: /es/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop, validación, validaciones
description: Este artículo presenta cómo usar validaciones en columnas en GridDesktop.
---

{{% alert color="primary" %}} 

En uno de nuestros temas anteriores, hemos discutido sobre las validaciones, pero eso fue en el contexto de [Validaciones en Hojas de Cálculo](/cells/es/net/working-with-validations-in-worksheets/) (para obtener información general sobre la validación y los modos de validación, los desarrolladores pueden consultar este tema). En este tema, explicaremos las validaciones con respecto a las columnas. Con esta función, los desarrolladores pueden aplicar una regla de validación en cualquier columna de la hoja de cálculo. Analicémoslo en detalle.

{{% /alert %}} 
## **Añadiendo Validación de Columna**
Para agregar cualquier tipo de validación a una columna, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- **Agregue** una **Validación** deseada a cualquier columna

**IMPORTANTE:** Para obtener más información sobre los tipos de validación (o modos de validación como **Validación Requerida**, **Validación de Expresiones Regulares** y **Validación Personalizada**) e implementar **Validación Personalizada**, consulte [Trabajar con Validaciones en Hojas de Cálculo.](/cells/es/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Accediendo a la Validación de Columna**
Para acceder a una validación específica de columna, siga los siguientes pasos:

- Acceda a una **Hoja de cálculo** deseada
- Acceda a una **Validación** específica de columna en la **Hoja de Cálculo**
- Edite los atributos de la **Validación**, si es necesario



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Eliminando Validación de Columna**
Para quitar una validación de columna específica de la hoja de cálculo, siga los pasos a continuación:

- Acceda a una **Hoja de cálculo** deseada
- Elimine una **Validación** de columna específica de la **Hoja de cálculo**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
