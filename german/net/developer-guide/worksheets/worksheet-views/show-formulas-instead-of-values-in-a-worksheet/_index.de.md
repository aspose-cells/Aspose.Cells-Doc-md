---
title: Statt Werte in einem Arbeitsblatt Formeln anzeigen
type: docs
weight: 20
url: /de/net/show-formulas-instead-of-values-in-a-worksheet/
description: In diesem Artikel finden Sie Beispielfunktionen, um mit der C# API oder der .NET Bibliothek programmgesteuert Formeln statt Werte in einem Excel Arbeitsblatt oder einer Tabelleneinheit anzuzeigen.
---

{{% alert color="primary" %}}

In Microsoft Excel ist es möglich, Formeln anstelle von berechneten Werten anzuzeigen, indem Sie die Option **Formeln anzeigen** im **Formeln**-Menüband verwenden. Wenn Formeln angezeigt werden, zeigt Microsoft Excel die Formeln im Arbeitsblatt an. Sie können das Gleiche mit Aspose.Cells erreichen.

{{% /alert %}}

Aspose.Cells bietet eine [**Worksheet.ShowFormulas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/showformulas)-Eigenschaft. Setzen Sie diese auf **true**, um Microsoft Excel anzuweisen, Formeln anzuzeigen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ShowFormulasInsteadOfValues-1.cs" >}}
