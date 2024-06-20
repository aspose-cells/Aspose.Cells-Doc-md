---
title: Libérer les ressources non gérées du classeur
type: docs
weight: 290
url: /fr/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells fournit la méthode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) pour libérer les ressources non gérées de l'objet [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Le modèle de libération est utilisé uniquement pour les objets qui accèdent à des ressources non gérées, telles que les handles de fichier et de canalisation, les handles de registre, les handles d'attente ou les pointeurs vers des blocs de mémoire non gérée. Cela est dû au fait que le ramasse-miettes est très efficace pour réclamer des objets managés inutilisés, mais qu'il est incapable de réclamer des objets non gérés.

{{% /alert %}} 
## **Libérer les ressources non gérées du classeur**
L'exemple de code suivant montre comment utiliser la méthode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
