---
title: Åtkomst till textrutan via namn med Golang via C++
linktitle: Tillgång till textfältet genom namnet
type: docs
weight: 230
url: /sv/go-cpp/access-the-text-box-by-the-name/
description: Lär dig hur man får åtkomst till en text box via dess namn med Aspose.Cells for C++.
---

## Åtkomst till textlådan med namnet

Tidigare kunde textlådor nås via index från [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/go-cpp/worksheet/gettextboxes/)-samlingen, men nu kan du också få åtkomst till textlådan via dess namn i denna samling. Det är ett bekvämt och snabbt sätt att få åtkomst till din textlåda om du redan känner till dess namn.

Följande exempel kod skapar först en text låda och tilldelar den text och ett namn. Sedan, i nästa steg, får vi åtkomst till samma textlåda via dess namn och skriver ut dess text.

### C++-kod för att få åtkomst till textlådan via namn

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessTheTextBoxByTheName.go" >}}
### Konsoloutput som genereras av provkoden

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
