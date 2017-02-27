Requirements
============

* [Ansible](https://www.ansible.com/)
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

```
[server]
XXX.XXX.XXX.XXX ansible_ssh_user=root
YYY.YYY.YYY.YYY ansible_ssh_user=root
ZZZ.ZZZ.ZZZ.ZZZ ansible_ssh_user=root
```

*Note:* Ensure that all of the servers listed in your inventory file have valid licenses.

## **Step 2:**

Customize the domain names (in `/group_vars/all.yml`).

* **administrators.fantastico_f3.com:**
    * This is used for the administrators panel of **Fantastico F3**. This is the section where you (the host of the server) will manage **Fantastico F3** as a whole. i.e.: keep it updated, check up on scripts, manage feature sets, etc. It must be run as root and therefore suitably protected by means of secure authentication/authorization.
* **visitors.fantastico_f3.com**:
    * This is used for the visitors panel of **Fantastico F3**. This is the section where your users will install scripts.
* **domain-1.com**, **domain-2.com**, **domain-3.com**
    * These are the public websites into which **Fantastico F3** will install scripts.
    * You can add as many domains as you want.

## **Step 3:**

Execute the playbook.

```
$ ansible-playbook --inventory inventory playbook.yml
```

## **Step 4:**

Set the `root` password.

```
# passwd root
```

## **Step 5:**

Set the `ubuntu` password.

```
# passwd ubuntu
```

## **Step 6:**

Open the following URLs in your browser.

* `http://{{ domains.administrators }}`
    * **Username:** `root`
    * **Password:** (see **Step 4**)
* `http://{{ domains.visitors }}`
    * **Username:** `Ubuntu`
    * **Password:** (see **Step 5**)
