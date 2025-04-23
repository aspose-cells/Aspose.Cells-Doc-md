---
title: Scopri se il progetto VBA è Protetto
type: docs
weight: 20
url: /it/net/find-out-if-vba-project-is-protected/
---

## **Scoprire se il progetto VBA è protetto in C#**

Puoi verificare se il progetto VBA (Visual Basic Applications) del tuo file Excel è protetto o meno con Aspose.Cells utilizzando la proprietà [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected).

## **Codice di Esempio**

Il seguente codice di esempio crea un workbook e quindi verifica se il suo progetto VBA è protetto o meno. Poi protegge il progetto VBA e controlla di nuovo se il suo progetto VBA è protetto o meno. Si prega di consultare l'output della console per un riferimento. Prima della protezione, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) restituisce **false** ma dopo la protezione restituisce **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Output della console**

Questo è l'output della console del codice di esempio sopra per un riferimento.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
