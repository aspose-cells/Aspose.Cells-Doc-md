---
title: Instalar Aspose.Cells en Windows
type: docs
weight: 20
url: /es/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

A veces puedes enfrentar algunos problemas al instalar **Aspose.Cells** utilizando su paquete instalador (Aspose.Cells.msi...Paquete de Instalación de Windows) en **Windows Vista**. Este documento explica cómo podemos hacer frente a esto e implementar la instalación exitosa del componente. En realidad, el instalador de **Aspose.Cells** necesita crear una carpeta virtual en IIS para el despliegue de sus Demostraciones Web (Demos Asp.NET) en tu máquina, así que necesitas tener Privilegios de Administración antes de instalar **Aspose.Cells** utilizando su instalador. El instalador requiere acceso a nivel de administrador al sistema y debe estar explícitamente permitido hacerlo.

{{% /alert %}} 
## **Factores Posibles**
Normalmente, en **Windows Vista**, los productos/componentes que instalas/utilizas siempre se implementan bajo permisos de "usuario normal", incluso si eres un **Administrador**. Los programas solo tienen acceso limitado al sistema de archivos, incluso si has iniciado sesión como **Administrador**. Esto tiene algunos efectos secundarios desafortunados que normalmente no encontrarías en Windows XP cuando iniciabas sesión como **Administrador**.
## **UAC (Control de Cuentas de Usuario)**
**UAC** es parte de **Windows Vista** que te solicita permiso. El modo **UAC** (también conocido como **Modo de Aprobación de Administrador**) es un modo de operación que afecta principalmente la forma en que funcionan las cuentas de administrador. Cuando el **UAC** está activado (que es por defecto), debes dar permiso explícito a cualquier programa que desee usar poderes de "administrador". Cualquier programa que intente usar poderes de administrador sin tu permiso tendrá acceso denegado. El **UAC** también es necesario para otras características de seguridad de **Windows Vista**, incluido el **Modo Protegido** en Internet Explorer. El Modo Protegido de Internet Explorer protege tu computadora de páginas web maliciosas y otras vulnerabilidades relacionadas con la web, incluidas las desconocidas.

Cuando el modo **UAC** está habilitado, cada programa que ejecutes tendrá solo acceso de "usuario estándar" al sistema, incluso cuando hayas iniciado sesión como administrador. **Windows Vista** tiene la capacidad integrada de reducir automáticamente el potencial de vulnerabilidades de seguridad en el sistema. Lo hace automáticamente al habilitar una característica llamada **Control de Cuenta de Usuario** (o **UAC** por sus siglas en inglés). **UAC** obliga a los usuarios que forman parte del grupo de administradores locales a funcionar como si fueran usuarios regulares sin privilegios administrativos. Aunque **UAC** mejora claramente la seguridad en **Windows Vista**, en algunos escenarios podrías querer deshabilitarlo, por ejemplo al realizar demostraciones frente a una audiencia (demostraciones que no están relacionadas con la seguridad, por ejemplo). Algunos usuarios domésticos podrían verse tentados a deshabilitar **UAC** debido al uso adicional de recursos de su sistema.
## **Pasos involucrados para la instalación exitosa del componente**
- Por favor asegúrese de que IIS esté instalado en su Vista antes de instalar **Aspose.Cells**. Es obligatorio porque el instalador de **Aspose.Cells** necesita crear una carpeta virtual en IIS para el despliegue de las Web Demos (Demos de Asp.NET).
- Necesitará desactivar el **UAC** (Control de Cuenta de Usuario). Debe asegurarse de tener **Privilegios de Administrador** con control total del sistema antes de instalar **Aspose.Cells**. De lo contrario, podría recibir un error n.º 2869 al instalar **Aspose.Cells** usando su instalador.

A continuación, algunas formas de lograr esto.
### **Usando la Línea de Comandos**
1. Busque cmd.exe en su directorio de Windows, luego haga clic derecho sobre él y seleccione Ejecutar como... **Administrador**
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **Usando el Panel de Control**
- Haga clic en Inicio
- Haga clic en Panel de Control
- Haga clic en Cuentas de Usuario y Protección Infantil
- Haga clic en Cuentas de Usuario
- Haga clic en Cambiar configuración de Control de Cuentas de Usuario
- Desmarque la casilla
- Haga clic en Aceptar

{{% alert color="primary" %}} 

Deberá reiniciar su computadora para que el cambio surta efecto. Este cambio afecta a todas las cuentas en la computadora, no solo a la suya.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
