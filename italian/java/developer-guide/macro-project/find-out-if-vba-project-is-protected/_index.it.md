---
title: Scopri se il progetto VBA è Protetto
type: docs
weight: 80
url: /it/java/find-out-if-vba-project-is-protected/
---

## **Possibili Scenari di Utilizzo**
Puoi verificare se il Progetto VBA (Visual Basic Applications) del tuo file Excel è protetto o meno con Aspose.Cells utilizzando il metodo [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected).
## **Codice di Esempio**
Il seguente codice di esempio crea un workbook e poi controlla se il suo progetto VBA è protetto oppure no. Quindi protegge il progetto VBA e controlla nuovamente se il progetto VBA è protetto oppure no. Si prega di consultare l'output della console per un riferimento. Prima della protezione, [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) restituisce **falso** ma dopo la protezione restituisce **vero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Output della console**
Questo è l'output della console del codice di esempio sopra per un riferimento.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
