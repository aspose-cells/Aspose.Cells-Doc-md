---
title: Libérer les ressources non gérées du classeur
type: docs
weight: 290
url: /fr/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells fournit la méthode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) pour libérer les ressources non managées de l'objet [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Le modèle de libération (dispose pattern) est utilisé uniquement pour les objets qui accèdent à des ressources non gérées, telles que les gestionnaires de fichiers et de tuyaux, les gestionnaires de registre, les gestionnaires d'attente ou les pointeurs vers des blocs de mémoire non gérée. Cela parce que le ramasse-miettes (garbage collector) est très efficace pour récupérer les objets gérés inutilisés, mais incapable de récupérer les objets non gérés.

{{% /alert %}} 
## **Libérer les ressources non gérées du classeur**
Le exemple suivant montre comment utiliser la méthode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
