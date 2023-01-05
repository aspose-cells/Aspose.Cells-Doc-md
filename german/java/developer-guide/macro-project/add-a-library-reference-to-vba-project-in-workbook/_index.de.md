---
title: Fügen Sie einen Bibliotheksverweis zum VBA-Projekt in der Arbeitsmappe hinzu
type: docs
weight: 10
url: /de/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 In Microsoft Excel können Sie dem VBA-Projekt einen Bibliotheksverweis hinzufügen, indem Sie auf klicken**Extras > Referenzen...** manuell. Es öffnet sich das folgende Dialogfeld, das Ihnen hilft, aus vorhandenen Referenzen auszuwählen oder Ihre Bibliothek selbst zu durchsuchen.

![todo: Bild_alt_Text](add-a-library-reference-to-vba-project-in-workbook_1.png)

 Aber manchmal müssen Sie den Bibliotheksverweis über Code zum VBA-Projekt hinzufügen oder registrieren. Sie können dies unter Aspose.Cells tun[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) Methode.

{{% /alert %}}

## **Fügen Sie einen Bibliotheksverweis zum VBA-Projekt in der Arbeitsmappe hinzu**

 Der folgende Beispielcode fügt dem VBA-Projekt der Arbeitsmappe zwei Bibliotheksverweise hinzu oder registriert sie[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
