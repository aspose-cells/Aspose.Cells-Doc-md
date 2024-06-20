---
title: Comprobar el número de versión del componente
type: docs
weight: 70
url: /es/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

En algunos casos, es posible preguntarse qué versión del producto se tiene. A menudo construimos nuevas correcciones (correcciones de errores para los escenarios de usuario que señalan) y las publicamos en los foros según su necesidad urgente. El número de versión consta de número de versión principal, número de versión secundaria y número de versión de corrección. Todos los componentes definidos deben ser enteros mayores o iguales a 0. El formato del número de versión es el siguiente:

número_principal.número_secundario.corrección , podemos aumentar una parte en 1 y crear una nueva versión. Normalmente, aumentamos la última parte en 1 y creamos una nueva corrección para publicarla en los foros para los usuarios.

Este documento describe algunas formas de comprobar qué versión del componente está instalada en su sistema.

{{% /alert %}} 
## **Comprobando el número de versión**
### **1) Forma Manual**
Si tiene la versión/corrección de Java (Aspose.Cells for Java), puede descomprimir el archivo jar de la biblioteca Aspose.Cells, abrir el archivo MANIFEST con el bloc de notas y buscar la cadena es decir., "Specification-Version: " para comprobar su valor.

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**Figura:** Comprobando el número de versión de la corrección de Java
### **2) Uso de las APIs**
También puede utilizar las siguientes APIs para obtener el número de versión del producto.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

