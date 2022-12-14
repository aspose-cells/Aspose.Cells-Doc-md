---
title: Afficher ou masquer les onglets dans Python
type: docs
weight: 30
url: /fr/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - Afficher les onglets masqués**
### **Masquer les onglets**
 Pour masquer les onglets à l'aide de**Aspose.Cells Java pour rubis** , appel**afficher les onglets masqués** module.

**Code Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Rendre les onglets visibles**
Rendez les onglets visibles avec la méthode setSheetTabBarHidden(false) de la classe Workbook.

**Code Python**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Hello World (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
