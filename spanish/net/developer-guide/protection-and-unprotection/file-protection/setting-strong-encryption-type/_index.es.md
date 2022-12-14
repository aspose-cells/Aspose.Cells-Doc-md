---
title: Configuración del tipo de cifrado fuerte
type: docs
weight: 60
url: /es/net/setting-strong-encryption-type/
---
{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) le permite cifrar y proteger con contraseña las hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos. Un proveedor de servicios criptográficos (o CSP) es un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es "Compatible con Office 97/2000". Este es un CSP con algunos problemas de seguridad conocidos públicamente. Las hojas de cálculo protegidas con el "cifrado débil (XOR)" o con el tipo de cifrado "Compatible con Office 97/2000" se pueden descifrar fácilmente.

Para superar este problema, utilice uno de los tipos de encriptación fuertes proporcionados por Microsoft Excel. Puede cambiar el tipo de cifrado al CSP más fuerte disponible. Para un cifrado fuerte, se requiere una longitud de clave mínima de 128 bits, por ejemplo, 'Microsoft Proveedor criptográfico fuerte'.

También puede cifrar y proteger con contraseña los archivos de Excel con un tipo de cifrado fuerte utilizando el Aspose.Cells API.

{{% /alert %}} 
## **Aplicación de cifrado con Microsoft Excel**
Para implementar el cifrado de archivos en Microsoft Excel (por ejemplo, 2007):

1.  Desde el**Instrumentos** menú, seleccione**Opciones**.
1.  Selecciona el**Seguridad** pestaña.
1.  Introduzca un valor para el**Contraseña para abrir** campo.
1.  Hacer clic**Avanzado**.
1. Elija el tipo de encriptación y confirme la contraseña.
## **Aplicación de cifrado con Aspose.Cells**
Los ejemplos de código a continuación aplican un cifrado fuerte en un archivo y establecen una contraseña.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
