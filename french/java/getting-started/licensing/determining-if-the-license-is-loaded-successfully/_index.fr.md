---
title: Détermination si la licence est chargée avec succès
type: docs
weight: 210
url: /fr/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells fournit la propriété [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) que vous pouvez utiliser pour déterminer si la licence est chargée avec succès ou non. Si vous appelez cette méthode avant de définir la licence, elle renverra false, et si vous appelez cette méthode après avoir défini la licence, elle renverra true, indiquant que la licence a été chargée avec succès.

{{% /alert %}}

## **Détermination si la licence est chargée avec succès**

Le code suivant accède à la méthode [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) avant de définir une licence et renvoie false. Ensuite, il charge la licence et accède à nouveau à la propriété qui renvoie maintenant true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus

{{< highlight java >}}

false

true

{{< /highlight >}}
