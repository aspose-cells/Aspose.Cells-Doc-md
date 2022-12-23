---
title: Editor de hojas de cálculo - Componentes
type: docs
weight: 50
url: /es/java/spreadsheet-editor-components/
---
**Tabla de contenido**

- [índice.html](#SpreadsheetEditor-Components-Index.html)
- [Vista de hoja de trabajo](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [Servicio de cargador](#SpreadsheetEditor-Components-LoaderService)
- [servicio de celdas](#SpreadsheetEditor-Components-CellsService)

El editor de hojas de cálculo HTML5 está construido a partir de unos pocos componentes que se unen para formar el sistema completo. Aquí describimos el propósito y el papel de cada uno.
### **índice.html**
Es una página JSF que describe la interfaz de usuario del editor y el punto final principal de nuestra aplicación. Toda la interacción que se realiza entre el navegador web y el servidor se realiza a través de este punto final.

Además de definir la interfaz de usuario, todos los servicios de back-end se adjuntan aquí mediante tecnologías JSF. Cuando el usuario interactúa con la interfaz de usuario, los eventos y los datos se transmiten de un lado a otro entre los servicios y el usuario para completar nuestras tareas, por ejemplo, exportar hojas de cálculo.

Tiene dos áreas principales de interés.

**Cinta**

El área de la barra de herramientas con pestañas en la parte superior se llama cinta, técnicamente. Contiene botones, menús desplegables, menús de radio, cuadros de texto y algunos campos ocultos que se utilizan para realizar muchas operaciones en la hoja de cálculo. Cuando se hace clic en estos botones, se envían comandos al servidor y se actualiza la hoja en consecuencia.

**Hoja**

La hoja son las filas y las columnas. Cuando se hace clic en las celdas, la cinta se actualiza en consecuencia sin enviar solicitudes al servidor, ya que todos los datos que necesita la cinta se adjuntan a cada celda. La cinta también realiza un seguimiento de la celda, la fila y la columna seleccionadas cuando el usuario navega por la hoja.

Cada celda tiene su propio editor en línea que se vuelve visible cuando una celda está en modo de edición.
### **Vista de hoja de trabajo**
Es un bean back-end JSF con ámbito de vista responsable de administrar los contenidos dinámicos de la interfaz de usuario descritos en index.html. Tiene controladores de eventos para solicitudes Ajax que se activan cuando el usuario interactúa con la interfaz de usuario.
### **WorkbookService**
El WorkbookService es un bean back-end JSF con ámbito de vista. Funciona como un componente de servicio y carga y descarga la hoja de cálculo con la ayuda de otros servicios. Tiene los siguientes extremos:

**en eso**

 Él**en eso** es**PostConstrucción** método que se ejecuta justo después de que el servidor de aplicaciones Java complete la creación del objeto. comprueba si**URL** parámetro en el mapa de parámetros de solicitud y carga la hoja de cálculo correspondiente desde la ubicación dada, si es posible.

**destruir**

Es responsable de limpiar todos los recursos adquiridos cuando ya no son necesarios.
### **Servicio de cargador**
Crea instancias de hojas de cálculo y las guarda en la memoria todo el tiempo que se necesitan.
### **servicio de celdas**
 Él**servicio de celdas** administra el caché de filas, columnas, celdas, formato y estructura de las hojas de cálculo.
