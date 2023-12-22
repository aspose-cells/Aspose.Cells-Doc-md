---
title: Fügen Sie einen Bibliotheksverweis auf das VBA-Projekt in der Arbeitsmappe hinzu
type: docs
weight: 10
url: /de/java/add-a-library-reference-to-vba-project-in-workbook/
description: Erfahren Sie, wie Sie über Aspose.Cells for Java API einen Bibliotheksverweis zu einem VBA-Projekt in einer Arbeitsmappe hinzufügen.
keywords: How to Add a library reference to VBA project in workbook in Java, Insert a library reference to VBA project in workbook using Java, Java Set library reference to VBA project in workbook. 
---
{{% alert color="primary" %}}

 In Microsoft Excel können Sie einen Bibliotheksverweis zum VBA-Projekt hinzufügen, indem Sie auf klicken**Extras > Referenzen...** manuell. Es öffnet sich das folgende Dialogfeld, das Ihnen hilft, aus vorhandenen Referenzen auszuwählen oder Ihre Bibliothek selbst zu durchsuchen.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Aber manchmal müssen Sie den Bibliotheksverweis über Code zum VBA-Projekt hinzufügen oder registrieren. Sie können dies unter der Rufnummer Aspose.Cells tun[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) Methode.

{{% /alert %}}

##  **So fügen Sie einen Bibliotheksverweis zu einem VBA-Projekt in einer Arbeitsmappe hinzu**

 Der folgende Beispielcode fügt zwei Bibliotheksverweise zum VBA-Projekt der Arbeitsmappe hinzu oder registriert sie[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
