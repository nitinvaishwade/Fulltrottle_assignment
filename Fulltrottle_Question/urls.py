"""Fulltrottle_Question URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_first.views import Index
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('app_first.urls'))
]







<div class="card mb-2">
    <div class="card-header">
        <h3 class="hd-3">
How Prepared do You Feel? </h3>
    </div>
    <div class="card-body">
        <div class="_title mb-2">
          
         After going through the learning challenge and exploring the resources, how prepared do you feel to install virtualization&#160;software?<BR><BR>Submit your response to see more resources that will help you prepare further. There is no right or wrong answer.
          
        </div>
        <textarea name="ans" id="ans" style="min-height: 150px; width: 100%; margin: 10px 0;" class="form-control"></textarea>
        <br />
      <button class="btn btn-primary mt-2 mb-3"
onclick="$(this).siblings('#item_explanation').show();">Submit</button> &nbsp;<button class="btn btn-primary mt-2 mb-3" onclick="$('textarea').val('');$('.explanation').hide();">Reset</button>
        <div id="item_explanation" navid="explanation" navtype="item"
            class="font16 py-2 explanation h position-relative clearboth px-3 ml-2" style="display: none;">
            <div class="mb-md break-all" tabindex="0"><BR>
                <span>
       <h3 class="heading_review d-inline confirm_message line_height3">Explanation</h3><hr>
                                                    <div class="explanation_content font17 pt-3">
                                <section class="sec_button inline" type="ebook-item" sub_type="text"><div class='ebook_item_text inline'>
                                For more information about installing virtualization&#160;software, you may find the following resources useful:<BR><BR><ul><li><a target="_blank" href="https://lrps.wgu.edu/provision/183626469" target="_blank" onclick="">Fischer, W. (n.d.). Network configuration in Virtual Box. Retrieved from Thomas-Krenn&#160;AG.<span class="link-icon"></span></a></li><li><a target="_blank" href="https://docs.netgate.com/pfsense/en/latest/" target="_blank" onclick="">Rubicon Enterprises, LLC&#160;(2019).&#160;pfSense Documentation. Retrieved from docs.netgate.com.<span class="link-icon"></span></a></li><li><a target="_blank" href="https://lrps.wgu.edu/provision/183627390" target="_blank" onclick="">VMware&#160;(2019). VMware&#160;Workstation 3.2. Retrieved from VMware.<span class="link-icon"></span></a></li><li><a target="_blank" href="https://lrps.wgu.edu/provision/183621823" target="_blank" onclick="">Wikibooks (2016). Virtual Box wikibook: Setting up a virtual machine.<span class="link-icon"></span></a></li><li><a target="_blank" href="https://lrps.wgu.edu/provision/183627631" target="_blank">Wikihow staff. (2019). How To Use VMWare Workstation. Retrieved from Wikihow.</a></li><li><a target="_blank" href="https://lrps.wgu.edu/provision/183627048" target="_blank" onclick="">Yaman, H. (2019). Hyper-V installation and configuration step-by-step. Retrieved from Veeam&#160;Software.<span class="link-icon"></span></a></li></ul><b><BR>Pluralsight Videos</b>:<BR><BR><ul><li><a target="_blank" onclick="" href="https://lrps.wgu.edu/provision/183456579" target="_blank">Davis, D. (2013). Windows Server 2012 Hyper-V New Features<span class="link-icon"></span></a>&#160;</li><li><a target="_blank" href="https://lrps.wgu.edu/provision/183447965" target="_blank">Liberman, E. (2011). Microsoft Server Virtualization: Hyper-V<span class="link-icon"></span></a>&#160;</li><li><a target="_blank" onclick="" href="https://lrps.wgu.edu/provision/183446680" target="_blank">Nash, J. (2013). Managing Hyper-V Using VMware's Multi-Hypervisor Manager<span class="link-icon"></span></a>&#160;</li><li><a target="_blank" onclick="" href="https://lrps.wgu.edu/provision/183446162" target="_blank">Shields, G. (2016). Implementing Windows Server 2016 Hyper-V.<span class="link-icon"></span></a>&#160;</li></ul></div></section></div>
                                                                        </span>
            </div>
        </div>
    </div>
</div>
