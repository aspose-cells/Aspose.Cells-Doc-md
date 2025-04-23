---
title: Kontrollera versionsnumret för komponenten
type: docs
weight: 70
url: /sv/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

I vissa fall kan du undra vilken version av produkten du har. Ofta bygger vi nya rättelser (buggrättelser för användarscenarier som de pekar ut) och lägger ut dem i forumen mot deras akuta behov. Versionsnumret består av huvudversionsnummer, mindre versionsnummer och hotfixversionsnummer. Alla definierade komponenter måste vara heltal större än eller lika med 0. Formatet för versionsnumret är följande:

huvudversion.minor.hotfix, vi kan öka en del med 1 och göra en ny version. Normalt ökar vi den sista delen med 1 och bygger en ny rättelse för att lägga ut den i forumen för användarna.

Detta dokument beskriver några sätt att kontrollera vilken version av komponenten som är installerad på ditt system.

{{% /alert %}} 
## **Kontrollera versionsnumret**
### **1) Manuellt sätt**
Om du har Java-version/rättelse (Aspose.Cells for Java), kan du packa upp Aspose.Cells-bibliotekets jar-fil, öppna MANIFEST-filen med anteckningar och söka efter strängen dvs., "Specifikationsversion:" för att kontrollera dess värde.

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**Figur:** Kontrollera versionsnumret för Java-rättelse
### **2) Användning av API:er**
Du kan också använda följande API:er för att få versionsnumret för produkten.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

{{< app/cells/assistant language="java" >}}
