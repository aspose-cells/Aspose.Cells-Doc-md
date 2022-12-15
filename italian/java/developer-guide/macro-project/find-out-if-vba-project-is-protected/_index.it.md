---
title: Scopri se il progetto VBA è protetto
type: docs
weight: 80
url: /it/java/find-out-if-vba-project-is-protected/
---
## **Possibili scenari di utilizzo**
 Puoi scoprire se il progetto VBA (Visual Basic Applications) del tuo file Excel è protetto o meno con Aspose.Cells usando[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)metodo
## **Codice di esempio**
 Il seguente codice di esempio crea una cartella di lavoro e quindi controlla se il relativo progetto VBA è protetto o meno. Quindi protegge il progetto VBA e controlla nuovamente se il suo progetto VBA è protetto o meno. Si prega di vedere l'output della sua console per un riferimento. Prima della protezione,[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) ritorna**falso** ma dopo la protezione, ritorna**VERO**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Uscita console**
Questo è l'output della console del codice di esempio precedente come riferimento.

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
