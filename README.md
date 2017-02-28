Requirements
============

* [Ansible](http://docs.ansible.com/ansible/)
* [https://netenberg.com/#fantastico-standalone.html](https://netenberg.com/#fantastico-standalone.html)

How to install?
===============

```
$ git clone --recursive git@github.com:mahendrakalkura/fantastico_f3.git
```

How to use?
===========

## **Step 1:**

Create your inventory file.

```
$ touch inventory
```

**Example:**

```
[server]
XXX.XXX.XXX.XXX ansible_ssh_user=root
YYY.YYY.YYY.YYY ansible_ssh_user=root
ZZZ.ZZZ.ZZZ.ZZZ ansible_ssh_user=root
```

**Note:** Ensure that all of the servers listed in your inventory file have valid licenses.

## **Step 2:**

Review the configurable parameters.

```
$ cat group_vars/all.yml
```

## **Step 3:**

Execute the playbook.

```
$ ansible-playbook --inventory inventory playbook.yml
```

## **Step 4:**

Open the following URLs in your browser.

* `http://XXX.XXX.XXX.XXX:8001`
    * **Username:** `{{ mod_auth_digest.administrators.username }}`
    * **Password:** `{{ mod_auth_digest.administrators.password }}`
    * **Reference:** `group_vars/all.yml`
* `http://XXX.XXX.XXX.XXX:8002`
    * **Username:** `{{ mod_auth_digest.visitors.username }}`
    * **Password:** `{{ mod_auth_digest.visitors.password }}`
    * **Reference:** `group_vars/all.yml`
