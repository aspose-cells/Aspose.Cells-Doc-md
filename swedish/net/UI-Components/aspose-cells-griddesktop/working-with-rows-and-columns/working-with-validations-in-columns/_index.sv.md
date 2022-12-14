---
title: Arbeta med valideringar i kolumner
type: docs
weight: 80
url: /sv/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 I ett av våra tidigare ämnen har vi diskuterat om valideringar men det var i samband med[Valideringar i arbetsblad](/cells/sv/net/working-with-validations-in-worksheets/) (för att ha allmän information om validerings- och valideringslägen kan utvecklare hänvisa till detta ämne). I det här ämnet kommer vi att förklara valideringar med avseende på kolumner. Med den här funktionen är det möjligt för utvecklare att tillämpa en valideringsregel på valfri kolumn i kalkylbladet. Låt oss diskutera det i detalj.

{{% /alert %}} 
## **Lägger till kolumnvalidering**
För att lägga till någon form av validering till en kolumn, följ stegen nedan:

-  Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**
-  Få åtkomst till alla önskade**Arbetsblad**
- **Lägg till** en önskad**Godkännande** till valfri kolumn

**VIKTIG:**För mer information om typerna av validering (eller valideringslägen som**Krävs validering**, **Validering av reguljära uttryck** och**Anpassad validering** ) och implementera**Anpassad validering** , se[Arbeta med valideringar i arbetsblad.](/cells/sv/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Åtkomst till kolumnvalidering**
För att komma åt en specifik kolumnvalidering, följ stegen nedan:

-  Få tillgång till en önskad**Arbetsblad**
-  Öppna en specifik kolumn**Godkännande** i**Arbetsblad**
-  Redigera**Godkännande** attribut, om så önskas



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Ta bort kolumnvalidering**
För att ta bort en specifik kolumnvalidering från kalkylbladet, följ stegen nedan:

-  Få tillgång till en önskad**Arbetsblad**
-  Ta bort en specifik kolumn**Godkännande** från**Arbetsblad**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
