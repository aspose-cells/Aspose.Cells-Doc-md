---
title: Fügen Sie eine Bibliotheksreferenz zum VBA Projekt in der Arbeitsmappe hinzu
type: docs
weight: 10
url: /de/java/add-a-library-reference-to-vba-project-in-workbook/
description: Erfahren Sie, wie Sie eine Bibliotheksreferenz zum VBA Projekt in der Arbeitsmappe über die API Aspose.Cells for Java hinzufügen
keywords: Wie fügt man eine Bibliotheksreferenz zum VBA Projekt in einer Arbeitsmappe in Java hinzu, fügt eine Bibliotheksreferenz zum VBA Projekt in einer Arbeitsmappe mit Java ein, setzt eine Bibliotheksreferenz zum VBA Projekt in einer Arbeitsmappe mit Java 
---

{{% alert color="primary" %}}

In Microsoft Excel können Sie manuell durch Klicken auf **Extras > Verweise...** eine Bibliotheksreferenz zum VBA-Projekt hinzufügen. Es öffnet sich ein Dialogfeld, das Ihnen dabei helfen wird, aus vorhandenen Verweisen auszuwählen oder Ihre Bibliothek selbst zu durchsuchen.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Manchmal müssen Sie jedoch die Bibliotheksreferenz zum VBA-Projekt durch Code hinzufügen oder registrieren. Dies können Sie mithilfe der Methode [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-) von Aspose.Cells tun.

{{% /alert %}}

## **Wie fügt man eine Bibliotheksreferenz zum VBA-Projekt in einer Arbeitsmappe hinzu**

Der folgende Beispielcode fügt oder registriert zwei Bibliotheksreferenzen im VBA-Projekt der Arbeitsmappe mithilfe der Methode [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-) hinzu.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
{{< app/cells/assistant language="java" >}}
