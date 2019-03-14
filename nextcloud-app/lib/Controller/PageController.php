<?php
namespace OCA\GarageDoor\Controller;

use OCP\IRequest;
use OCP\AppFramework\Http\TemplateResponse;
use OCP\AppFramework\Http\DataResponse;
use OCP\AppFramework\Controller;

class PageController extends Controller {
	private $userId;

	public function __construct($AppName, IRequest $request, $UserId){
		parent::__construct($AppName, $request);
		$this->userId = $UserId;
	}

	/**
	 * @NoAdminRequired
	 * @NoCSRFRequired
	 */
	public function index() {
		return new TemplateResponse('garagedoor', 'index');  // templates/index.php
	}

	/**
	 * @NoAdminRequired
	 */
	public function click() {
		return new DataResponse(shell_exec("GarageDoor --click"));
	}

}
