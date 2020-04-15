module.exports = {
  apps: [
    {
      script: "./components/plone/bin/zeoserver",
      args: "fg",
      name: "stradanove-plone-zeoserver",
      cwd: "/opt/stradanove/stradanove.buildout",
      interpreter:
        "/opt/stradanove/stradanove.buildout/components/plone/bin/python",
    },
    {
      script: "./components/plone/bin/instance1",
      args: "console",
      name: "stradanove-plone-instance1",
      cwd: "/opt/stradanove/stradanove.buildout",
      interpreter:
        "/opt/stradanove/stradanove.buildout/components/plone/bin/python",
    },
    {
      script: "./components/plone/bin/instance2",
      args: "console",
      name: "stradanove-plone-instance2",
      cwd: "/opt/stradanove/stradanove.buildout",
      interpreter:
        "/opt/stradanove/stradanove.buildout/components/plone/bin/python",
    },
//    {
//      script: "./components/varnish/bin/varnish-script",
//      args: "-F",
//      name: "stradanove-varnish",
//      cwd: "/opt/stradanove/stradanove.buildout",
//      exec_interpreter: "bash",
//    },
  ],
};

