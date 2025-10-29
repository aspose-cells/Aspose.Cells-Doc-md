---
title: 如何使用GridJs构建协作Excel编辑器
type: docs
weight: 260
url: /zh/java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor/
keywords: GridJs、协作、Excel编辑器、电子表格、Java
description: 本文介绍如何使用Aspose.Cells.GridJs for Java构建协作Excel编辑器。
aliases:
  - /java/aspose-cells-gridjs/collaborative-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-spreadsheet-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor-using-gridjs/
---

# 协作Excel编辑器指南

## 架构概述

 下图显示了GridJs如何实现多用户协作编辑， 
 一个Spring Boot后台、WebSocket通信以及用于状态管理的MySQL数据库。

![GridJs协作架构](gridjs_collaborative_architecture.png)

## 先决条件

 在开始之前，请确保已安装以下内容：

- **Java 8+**  
- **Maven**  
- **MySQL**（或其他支持的SQL数据库）  
-（可选）**Docker**，如果你喜欢在容器中运行  
- 有效的**Aspose.Cells许可证**（或[临时许可证](https://purchase.aspose.com/temporary-license)）  

---

## Step 1: Clone the Demo Project

Clone the official [Aspose.Cells GridJs demo repository](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs.Collaborative):

```bash
git clone https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java.git
cd Aspose.Cells-for-Java/Examples.GridJs.Collaborative
```

---

## Step 2: Configure Collaborative Mode

Open the [`src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties) file and adjust the settings:

```properties
# Directory containing spreadsheet files
testconfig.ListDir=/app/wb

# Directory for storing cache files
testconfig.CachePath=/app/grid_cache

# Aspose.Cells license file
testconfig.AsposeLicensePath=/app/license

# Enable collaborative mode
gridjs.iscollabrative=true

# Database connection (example: MySQL)
spring.datasource.url=jdbc:mysql://localhost:3306/gridjsdemodb?createDatabaseIfNotExist=true&useUnicode=true&serverTimezone=UTC&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
spring.sql.init.platform=mysql
```

这样可以让多个用户同时编辑同一电子表格。  
更改存储在数据库中，并在客户端之间实时同步。

---

## Step 3: Run the Application

Run with Maven:

```bash
mvn spring-boot:run
```

或者直接从主类：

```
src/main/java/com/aspose/gridjsdemo/usermanagement/UserManagementApplication.java
```

---

## Step 4: Test Collaborative Editing

Open your browser and navigate to:  
👉 `http://localhost:8080/gridjsdemo/list`

Steps:

1. A login page appears. Click **Create User** to register User1 and log in. You will then see the file list.  
2. Open a file from the list. The spreadsheet editor will load.  
3. Copy the same URL into another browser window. It will redirect to the login page. Create User2 and log in.  
4. Both users now see the same spreadsheet.  
5. If User1 edits the spreadsheet, User2 will see the changes in real time.  
6. If User2 edits, User1 will see the changes as well.  
7. Users can also download and save the file.  

---

## 第五步：在Docker中运行（可选）

如果在Docker中运行，请编辑 [`docker-compose.yml`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/docker-compose.yml) 的第10行，以映射许可证文件。  

例如，如果您的许可证文件在 `C:/license/aspose.lic`：

```yaml
volumes:
  - C:/license/aspose.lic:/app/license  # optional: set Aspose license file
```

这将本地文件映射到容器中。

然后构建并运行：

```bash
docker-compose up --build
```

访问应用：  
👉 `http://localhost:8080/gridjsdemo/list`

---

## Key Configuration Details

### 1. Enable Collaborative Mode

In [`/src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties):

```properties
gridjs.iscollabrative=true
```

在服务器端配置 [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java)：

```java
@Bean
public GridJsOptions gridJsOptions() {
    //..... other options
    //here we shall set true for collaborative mode
    options.setCollaborative(true);
    return options;
}
```

或全局设置：

```java
Config.setCollaborative(true);
```

在客户端加载选项 [`/src/main/resources/templates/file/index.html`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/templates/file/index.html)：

```js
const option = {
    //..... other options
    //here we shall set true for collaborative mode
    isCollaborative: true
    //..... other options
};
```

---

### 2. User System Integration

The demo uses **Spring Security** for a simple user system.  

You must provide a `CoWorkUserProvider` implementation to connect GridJs with your user system:

In server-side config [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

For example: here we defined MyCustomUser to implement all the interfaces in CoWorkUserProvider.

```java
@Bean
public CoWorkUserProvider currentUserProvider() {
    return new MyCustomUser();
}
```


在 [`/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java)：

```java
public class MyCustomUser implements CoWorkUserProvider {
    //Get the current login user name
    @Override
    public String getCurrentUserName() {
        return getCurrentUser().getUsername();
    }

    //Get the current login user Id
    @Override
    public Long getCurrentUserId() {
        return getCurrentUser().getUserId();
    }

    //Get the current login user permission
    @Override
    public CoWorkUserPermission getPermission() {
        return CoWorkUserPermission.EDITABLE;
    }

    private static CustomUserDetails getCurrentUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication != null && authentication.getPrincipal() instanceof CustomUserDetails) {
            return (CustomUserDetails) authentication.getPrincipal();
        }
        throw new IllegalStateException("User not authenticated");
    }
}
```

---

### 3. WebSocket Configuration

The demo uses **Spring WebSocket** with STOMP.  

Example config:

In [`/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java):

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic");
        config.setApplicationDestinationPrefixes("/app");
        config.setUserDestinationPrefix("/user");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

GridJs 期望 `messageTopic` 与默认的 "/topic/opr" 匹配：

```java
com.aspose.gridjs.Config.setMessageTopic("/topic/opr");
```

或者：

```java
@Bean
    public GridJsOptions gridJsOptions() {
	//.... other options
    	options.setMessageTopic("/topic/opr");
    	//.... other options
        return options;
    }
```

在客户端：

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws','/app/opr','/user/queue','/topic/opr');
```

这里，`/GridJs2/msg` 对应于定义的路由路径  
[`src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java)：

```java
@RequestMapping("/GridJs2/msg")
```

#### 使用自定义WebSocket路径的示例

如果您的服务器使用不同的配置：

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic_gridjs");
        config.setApplicationDestinationPrefixes("/app_gridjs");
        config.setUserDestinationPrefix("/user_gridjs");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws_gridjs")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

那么您必须设置：

**服务器端**：

```java
com.aspose.gridjs.Config.setMessageTopic("/topic_gridjs/opr");
```

或

```java
    @Bean
    public GridJsOptions gridJsOptions() {
	//.... other option
    	options.setMessageTopic("/topic_gridjs/opr");
    	//.... other option
        return options;
    }
```

**客户端**：

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws_gridjs','/app_gridjs/opr','/user_gridjs/queue','/topic_gridjs/opr');
```

setCollaborativeSetting的详细文档可以在[这里](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/)找到

> ⚠️ 注意：默认情况下，演示配置可以开箱即用。  
仅当您的应用自定义WebSocket端点时，才需要额外的配置。  

还要记住：协作模式**不支持**懒加载。  
不要启用`Config.setLazyLoading(true)`。

---

## Additional Notes


- We can add **file uploads** to load and edit spreadsheet file from upload directory.  
- Integrate with **cloud storage** like AWS S3 or Azure Blob.  

---

## 结论

使用Aspose.Cells.GridJs，您可以快速构建功能强大的**协作Excel编辑器**。  
Java后台、GridJs前端、SQL存储和WebSocket消息的结合，确保了可靠的实时电子表格编辑。

---

## Resources

- [Product Page](https://products.aspose.com/cells/java)  
- [Documentation](https://docs.aspose.com/cells/java/aspose-cells-gridjs/)  
- [API Reference](https://reference.aspose.com/cells/java/com.aspose.gridjs/)  
- [Support Forum](https://forum.aspose.com/c/cells)  
- [Free Online Apps](https://products.aspose.app/cells/family)  
