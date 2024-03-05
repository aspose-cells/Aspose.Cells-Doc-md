---
title: Kontrollera komponentens versionsnummer
type: docs
weight: 70
url: /sv/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

I vissa fall kanske du undrar vilken version av produkten du har. Ofta bygger vi nya korrigeringar (buggfixar för de användarscenarier som de pekar ut) och lägger upp dem i forumen mot deras behov akut. Versionsnumret består av huvudversionsnummer, mindre versionsnummer och snabbkorrigeringsversionsnummer. Alla definierade komponenter måste vara heltal större än eller lika med 0. Formatet för versionsnumret är som följer:

major.minor.hotfix , vi kan öka en del med 1 och göra en ny version. Normalt ökar vi den sista delen med 1 och bygger en ny fix för att lägga upp den i forumen för användarna.

Det här dokumentet beskriver några sätt att kontrollera vilken version av komponenten som är installerad på ditt system.

{{% /alert %}} 
## **Kontrollerar versionsnumret**
### **1) Manuellt sätt**
Om du har Java version/fix (Aspose.Cells for Java), kan du packa upp Aspose.Cells biblioteksjar-filen, öppna MANIFEST-filen med anteckningsblock och söka i strängen, dvs. "Specifikation-Version: " för att kontrollera dess värde.

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**Figur:** Kontrollerar versionsnumret för Java-fixen
### **2) Använda API:erna**
Du kan också använda följande API:er för att få produktens versionsnummer.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

